import random
import imp.genetics as gns
import imp.mth as math

## File where all creature classes are kept

class OrganismV2:
  '''Mostly Genome-Reliant Organism. Refer to code for genotype -> phenotype translations. Eventually will make a not hardcoded at all organism, but for V2 this is enough.'''

  def __init__(self, genome="", startingLineageName="", dieOnTurn=False):
    self.genome = genome
    self.decGenome = gns.decode(genome)
    self.sln = startingLineageName
    self.lineage = startingLineageName + "-"
    self.age = 0
    self.energy = 10
    self.dieOnTurn = dieOnTurn
    try:
      # added self.defense purely to avoid error throwing
      self.defense = 0

      # moved to the top for performance reasons
      self.photosynth = math.round_up(self.decGenome[3]/31.5) == 0 # make photosynthesis require AAA so it isn't easy to evolve (but can still happen)
      
      self.eatingSkill = self.decGenome[1] # arbitrary thing ig. no better ideas

      self.consumer = self.decGenome[6] > 54 and self.eatingSkill > 0 # arbitrary high value so it doesn't develop in plants easily (but also not as hard to mutate into as photosynthesis)
      if not self.photosynth and not self.consumer:
        raise Exception("bad") # for performance reasons. the creatures will die eventually and food should be relatively abundant so it doesn't matter if we kill the ones that are incapable of getting energy

      self.sex = int(math.round_up(self.decGenome[0]/31.5)) # 1m 2f 0a
      self.mateAttemptBias = int(float(self.decGenome[2]*-1)/31.5) # brain moment
      self.defense = int((self.eatingSkill+self.decGenome[4])/2) #averaging eatskill and body armor because it can 1 not die and 2 bite back/defend itself
      self.photosynthesis_effectivity = self.decGenome[5]-int(self.decGenome[4]/3) # can't get much sunlight if you're covered in armor
      self.attractedToWhichCodon = self.decGenome[7]
      self.matingStandards = self.decGenome[8] # basically seedchance on asexual organisms but on sexual reproducing ones it determines the level a codon should be for mating to occur
      self.matingStandardsAboveOrBelow = self.decGenome[9] > 32 #true is above matingStandards, false is below matingStandards

      if self.photosynth:
        self.lineage = self.lineage + "P" + str(self.photosynthesis_effectivity)
      if self.consumer:
        self.lineage = self.lineage + "C" + str(self.eatingSkill)
      self.lineage = self.lineage + "D" + str(self.defense)
      if self.matingStandardsAboveOrBelow and self.sex > 0:
        self.lineage = self.lineage + "-" + str(self.attractedToWhichCodon) + "/+" + str(self.matingStandards)
      elif self.sex > 0:
        self.lineage = self.lineage + str(self.attractedToWhichCodon) + "/-" + str(self.matingStandards)
      else:
        self.lineage = self.lineage + "ASX" + str(self.matingStandards)
      

    except:
      self.dieOnTurn = True # If it causes an error, we don't need i (Eli, 2023)
      # basically yes. that means a stop codon happened somewhere and the returned decoded genome is incomplete so the organism is basically doomed so we can kill off the ones that are "genetically unstable"

  def __str__(self):
    return self.lineage

  def __repr__(self):
    return self.lineage
  
  def turn(self, creatureLookingForMate):
    self.age += 1
    self.energy -= 1
    if (self.age > 10):
      self.energy -= (self.age-10)
    # based off V1 secondary consumer code
    choice = 0

    if self.dieOnTurn:
      return 0
    
    if isinstance(creatureLookingForMate, OrganismV2):
      try:
        attracted = ((creatureLookingForMate.decGenome[self.attractedToWhichCodon]-self.age > self.matingStandards and self.matingStandardsAboveOrBelow) or (creatureLookingForMate.decGenome[self.attractedToWhichCodon]-self.age < self.matingStandards and not self.matingStandardsAboveOrBelow))
      except:
        attracted = False
    else:
      attracted = False
    
    if isinstance(creatureLookingForMate, OrganismV2) and attracted and not creatureLookingForMate.dieOnTurn and (self.energy > 6) and creatureLookingForMate.sex != self.sex and self.sex > 0:
      self.energy -= 4
      return 1
    elif self.sex == 0 and random.randint(0, 63) < self.matingStandards and (self.energy > 6):
      self.energy -= 4
      return 1
    if (self.energy > 5+self.mateAttemptBias) and (self.sex > 0):
      self.energy -= 1
      return 2
    if (self.energy >= 3) and (self.energy <= 6) and self.consumer:
      self.energy -= 1
      return 3
    elif self.photosynth:
      return 4

    return 0
  
class Producer:
  '''Producer'''

  def __init__(self, age=0, genome="CGTTAAAAACGTTAA"):
    self.food = True
    self.age = age # Hello
    self.genome = genome
    self.decGenome = gns.decode(genome)
    try:
      try:
        self.seedchance = (self.decGenome[0]-self.decGenome[2])*int(self.decGenome[3]/31)
      except:
        self.seedchance = self.decGenome[0]
    except:
      self.seedchance = 1


  def turn(self):
    self.age += 1

  def getAge(self):
    return self.age

class SecondaryConsumer:
  '''Secondary Consumer
  Genotypes:
  Sex: 0
  Body: 1
  Strength: 2
  Agility: 3
  Mate Request Attractiveness Bias: 4
  Mate Attempt Bias: 5
  Defense: 6
  Stop Codon: 7
  
  Phenotypes:
  Hunting Skill: (2+3)-1
  Sex: 0/num_31.5 M=1 F=2
  Attractiveness: 1+3
  Brain: {4,5}
  '''
  def __init__(self, age=0, genome=""):
    self.age = age
    self.energy = 5 + (self.age * 1.5)
    self.genome = genome
    self.decGenome = gns.decode(genome)
    try:
      self.dienextturn = False
      self.sex = math.round_up(self.decGenome[0]/31.5)
      self.strength = (self.decGenome[2]+self.decGenome[3])-self.decGenome[1]
    except:
      self.dienextturn = True
      self.sex = 0
      self.strength = 0
    try:
      self.attractiveness = self.decGenome[1]+self.decGenome[3]
      self.attractive_standards = self.decGenome[4]
      self.mateAttemptBias = self.decGenome[5]
    except:
      self.attractiveness = 0
      self.attractive_standards = 0
      self.mateAttemptBias = 0

  def turn(self, mate_request_attractiveness, mate_request_sex):
    self.age += 1

    choice = 0

    m_a_bias = int(float(self.mateAttemptBias*-1)/31.5)
    
    if mate_request_attractiveness-self.age > self.attractive_standards and (self.energy > 4) and mate_request_sex != self.sex:
      self.energy -= 4
      choice = 1
    if (self.attractiveness != 0) and (self.energy > 5+m_a_bias) and (choice == 0):
      self.energy -= 1
      choice = 2
    if (self.energy >= 2) and (self.energy <= 4) and (choice == 0):
      self.energy -= 1
      choice = 3

    return choice
    
    
    


class PrimaryConsumer:
  '''Primary consumer'''
  '''
  Genotypes:
  Eat Chance Modifier 1: 0
  Eat Chance Modifier 2: 1
  Mouth Size: 2
  Reproductive Speed: 3
  Resource Management: 4
  Defense: 5
  Stop Codon: 6
  
  Phenotypes:
  Eating chance: (0/1)*2
  Mating chance: (3/4+2)
  Predator Safety: 5
  '''
  def __init__(self, age=0, genome="ATCCTCTCCCTTAACATGTAA"):
    self.age = age
    self.energy = 5 + (self.age * 1.5)
    self.madeKids = False
    self.eaten = None
    self.genome = genome
    self.decGenome = gns.decode(genome)
    try:
      self.dienextturn = False
      self.eatchance = (self.decGenome[0] / self.decGenome[1])*self.decGenome[2]
    except:
      self.dienextturn = True
      self.eatchance = 0
    try:
      self.matechance = (self.decGenome[3] /
                           (self.decGenome[4] + self.decGenome[2]))
    except:
      self.matechance = 0
      self.rizz = False
    try:
      self.defense = self.decGenome[5]
    except:
      self.defense = 0

  def turn(self, ismate, isfood):
    self.eaten = False
    self.age += 1
    self.energy -= 1

    if self.age > 10:
      #Old Age Tester
      ismate = False
      self.energy -= 3
    
    if ismate and self.age > 3 and self.energy>4: # Age test, energy test for amting
      # Mating test
      self.energy -= 7 # Mating takes energy
      self.madeKids = True # No idea why this is here
    elif isfood:
      # Eating food
      
      self.energy += 2 # Food gives energy
      self.eaten = True # For debugging ig?

class Decomposer:
  '''A decomposer organism
  Genotype:
  Spores: 0                      Default: 12
  Spore spreadability: 1         Default: 15
  Energy extraction: 2           Default: 16
  Energy replenishment: 3        Default: 12
  Stop: 4
  '''

  def __init__(self, age=0, genome="ATAATTCAAATATGA"):
    self.age = age
    self.energy=3
    self.spread = False

    # Genome data decoding
    self.genome = genome
    self.decGenome = gns.decode(genome)
    try:
      self.sporechancegen = (self.decGenome[0])*(self.decGenome[1])//10
    except:
      self.sporechancegen = 0 # Nonsense mutation check
    
    try:
      self.energyExt = self.decGenome[2]
    except:
      self.energyExt = 0 # Nonsense mutation check
    
    try:
      self.energyRep = self.decGenome[3]
    except:
      self.energyRep = 0 # Nonsense mutation check

  
  def turn(self, soilFert, ismate, ldlist):
    # Turn code
    self.age += 1
    self.energy -= 1
    self.spread = False

    if self.age > 6:
      self.energy -= self.age-5
      #Old Age Tester
      if self.age > 10:
        ismate = False
      self.energy -= math.round_up(self.age/2)
    if self.age>2 and ismate:
      self.spread = True
      self.energy -= 6

    # Energy extraction from soil
    self.energy+=float(soilFert)*(int(self.energyExt)/ldlist)
    self.energy=math.round_up(self.energy)


## END OF FILE ##
