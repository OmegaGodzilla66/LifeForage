# Another user-only tool - not used by the project itself
# NOTE: This only works with default-organism v3 or higher
import imp.genetics as gns
import imp.mth as math

decGenome = gns.decode(input("> "))

lineage = ""

print(decGenome)

# added defense purely to avoid error throwing
defense = 0

      # moved to the top for performance reasons
photosynth = math.round_up(decGenome[3]/31.5) == 0 # make photosynthesis require AAA so it isn't easy to evolve (but can still happen)
      
eatingSkill = decGenome[1] # arbitrary thing ig. no better ideas

consumer = decGenome[6] > 54 and eatingSkill > 0 # arbitrary high value so it doesn't develop in plants easily (but also not as hard to mutate into as photosynthesis)

sex = int(math.round_up(decGenome[0]/31.5)) # 1m 2f 0a


defense = int((eatingSkill+decGenome[4])/2) #averaging eatskill and body armor because it can 1 not die and 2 bite back/defend itself
photosynthesis_effectivity = decGenome[5]-int(decGenome[4]/3) # can't get much sunlight if you're covered in armor
attractedToWhichCodon = decGenome[7]
matingStandards = decGenome[8] # basically seedchance on asexual organisms but on sexual reproducing ones it determines the level a codon should be for mating to occur
matingStandardsAboveOrBelow = decGenome[9] > 32 #true is above matingStandards, false is below matingStandards

if photosynth:
  lineage = lineage + "P" + str(photosynthesis_effectivity)
if consumer:
  lineage = lineage + "C" + str(eatingSkill)
lineage = lineage + "D" + str(defense)
if matingStandardsAboveOrBelow and sex > 0:
  lineage = lineage + "-" + str(attractedToWhichCodon) + "/+" + str(matingStandards)
elif sex > 0:
  lineage = lineage + str(attractedToWhichCodon) + "/-" + str(matingStandards)
else:
  lineage = lineage + "ASX" + str(matingStandards)
print(lineage)
