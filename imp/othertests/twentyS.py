##Essentially what this would do is provide a playground for developers to add their own tests with LifeForage, such as my virus immunity simulator. 
import random
import imp.genetics as gns
import imp.mth as math  #omg meth???

class Organism20S:
  '''A *very* simple organism, meant for the 20S Virus Immunity simulator
  Genome: 
  0: Energy Consumptiion - 30/64
  1: Reproduction (asexual bc I'm lazy) 20/64
  2: Virus Protection
  3: stop codon
  (If these mutations arise:)
  4: If < 10, kill. If >60, immunity+1. Else, no effect. 
  5: If < 25: kill. If >60 add immunity+1. Else, no effect. 
  6: If < 50: kill. IF >60 add immunity+5. ELse, no effect. 
  If genome length is greater than 6, kill. 

  A note on the length of the genome:
  The genome is meant to be extremely long, however most of the characters are not actually used. The entire genome with used characters is actually just 12 characters. The rest take place after a stop codon (TAA) meaning that the majority of the the data is not actually used. 
  '''

  def __init__(self, age=0, genome=""):
    self.food = True
    self.infected = False
    self.age = age # amongus
    self.genome = genome
    self.infected=False
    self.energy=3
    self.decGenome = gns.decode(genome)
    try:
      self.seedchance = (self.decGenome[0])
    except:
      self.seedchance = 0

  def turn(self,newinfection=False):
    self.age+=1
    if newinfection and not self.infected:
      self.infected=True
      self.infectedTurns=-5

    if self.infected:
      eloss=self.infectedTurns+random.randint(0,10)
      if not eloss<0:
        self.energy-=eloss


class WorldEnv20S:
  def __init__(self,virusGenome='CTGCTGTGA'):
    '''Virus Phenotypes:
    Spreadability: 0 - 30
    Death token: 1 - 20
    Stop codon: 4
    '''
    self.virusGenome=virusGenome
    

  def world_turn(self,orglist):
    numinfected=0
    gnT=gns.mutate(self.virusGenome)
    
    while len(gns.decode(gnT))!=1:
      
      gnT=gns.mutate(self.virusGenome)
    self.virusGenome=gnT
    vdc=gns.decode(self.virusGenome) #virus decoded genome
    for org in orglist:
      if org.decGenome[2]>vdc[0] and random.randrange(0,2)==1:
          org.infected=True
      if org.infected:
        numinfected+=1
        org.energy-=(vdc[1]//10)
    print("There are ",numinfected," infected organisms in  the simulation")

def lifeturn20S(orglist,worldenv):
  '''A turn in a life, with an organism list. '''
  # Start varriable declaration
  Pop = 0
  
  iter = 0
  worldenv.world_turn(orglist)
  for entity in orglist:
    # Life Cycle
    if isinstance(entity, Organism20S):  #x in rlist is fix to index out of bounds error
      Pop += 1
      MATE_KEY = entity.seedchance > random.randint(0, 64)

      entity.turn()  # Turn

      # Mating
      if (entity.age > 2) and MATE_KEY and Pop<250: #Population checks
        orglist.append(Organism20S(genome=gns.mutate(entity.genome)))

      # Death
      if entity.age > 5:
        Pop-=1
        orglist.pop(iter)

      # Energy Consumption, and life tax
      #entity.energy-=1
      if entity.energy<=0:
        Pop-=1
        orglist.pop(iter)
      if entity.age>10:
        entity.energy-=entity.age//3
        
    iter += 1
  print("Existing Organisms: ",Pop)

def startCiv20S(orgnum,customGenome=False):
  #Starting list vals
  orglist = []
  for i in range(orgnum):
    # Add organisms
    if customGenome:
      pass
    else:
      genome="CTGCCAAAGTAATGAGTAGCTGTACGT"
    orglist.append(Organism20S(age=2,genome=genome))

  
  return orglist

def init_20S():
  orglist=startCiv20S(int(input("Enter Number of Organisms\n> ")))
  we=WorldEnv20S()
  while len(orglist)>0:
    lifeturn20S(orglist,we)
  print("Number of Organisms has reached 0")
  exit()
