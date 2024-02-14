import random
import imp.org as org
import imp.genetics as gns
import imp.mth as math
import imp.environment as env
import imp.othertests.twentyS as tS
import imp.othertests.sixteenD as sD

##Startvals (old sim)
SIZE = 10
SIZEKEY = 5
DECKEY = 2
C2KEY = 100
print(
    "The following block of text is important - Please read if this is your first time using LifeForage Delta"
)
input("> Ok")
print('''Welcome to LifeForage Delta - A Genetics Engine for the Future
Warning - As this is in beta, not all features will make sense. Additional prints may happen in order for continus debugging and feature improvements. 
Organism Level 1 - Not comatible with any existing levels of LifeTurn

Organism Level 2 - Compatible with Lifeturn V1
Features:
* Starts with existing population of 4 unique organisms (based on genome size, and interpretation)
* Shows population values
* Basic neural network for 2C
* Decomposers
* Preset genomes for all organisms
* Evolution
* LifeForage mutation engine
Organism Feature Level 1 is NOT compatible with any other LifeTurns. 

Organism Level 3 - Compatible with Lifeturn V2
Features:
* Starts with existing population of 1 unique organism
* Prints individual organism genomes
* Other data presented (Main programmer's note: I don't actually know what I did, this project is from a year ago. genome_decoder.py is relatively well commented though and handles most of the printing, so probably check that out)
* Preset default genome
* Evolution
* LifeForage mutation engine

Organism Level 3 - Compatible with Lifeturn V3 - BETA
Features:
* Starts with existing population of 1 unique organism
* Prints organism genome of the HIGHEST POPULATION VALUE
* Automatic lineage tracking
* Population traccking for highest lineage
* Population tracking for total creature values
* Preset default genome
* Evolution
* LifeForage mutation engine
World Enviornment V0 - Compatible with Lifeturn V3 - ALPHA
Features:
* Photosynthesis effectiveness simulatiion
* Natural disasters
* Natural disaster customization. 

FOR BEGINNERS - Use lifeturn v1 and Organism level 2
''')


def startCiv():
    #Starting list vals
    orglist = []
    foodlist = []
    declist = []
    cons2list = []
    alternator_consumer2 = False
    for n in range(C2KEY):
        if (alternator_consumer2):
            pass
            # Male
            cons2list.append(
                org.SecondaryConsumer(
                    age=0, genome=gns.mutate("AACATTACCATCAAAGAAATGTGA")))
        else:
            pass
            # Female
            cons2list.append(
                org.SecondaryConsumer(
                    age=0, genome=gns.mutate("TTTATTACCATCAAAGAAATGTGA")))

        alternator_consumer2 = not alternator_consumer2

        for i in range(SIZE):
            # Add Primary Consumers
            orglist.append(org.PrimaryConsumer(age=random.randint(0, 9)))
            for i2 in range(SIZEKEY):
                # Add Resources
                foodlist.append(org.Producer(random.randrange(1, 4)))

        for i2 in range(DECKEY):
            # Add decomposers
            declist.append(org.Decomposer())

    return (foodlist, orglist, cons2list, declist)


def startCiv_v2():
    #Starting list vals
    orglist = []
    alternator_consumer2 = False
    for n in range(C2KEY):
        if (alternator_consumer2):
            # Male
            orglist.append(
                org.SecondaryConsumer(
                    age=0, genome=gns.mutate("AACATTACCATCAAAGAAATGTGA")))
        else:
            # Female
            orglist.append(
                org.SecondaryConsumer(
                    age=0, genome=gns.mutate("TTTATTACCATCAAAGAAATGTGA")))

        alternator_consumer2 = not alternator_consumer2

        for i in range(SIZE):
            # Add Primary Consumers
            orglist.append(org.PrimaryConsumer(age=random.randint(0, 9)))
            for i2 in range(SIZEKEY):
                # Add Resources
                orglist.append(org.Producer(random.randrange(1, 4)))

        for i2 in range(DECKEY):
            # Add decomposers
            orglist.append(org.Decomposer())

    return orglist


def startCiv_v3():
    orglist_v3 = []
    orgcount = int(input("How many organisms?\n> "))
    alternator = 0
    for i in range(0, orgcount):
        if (alternator == 0):
            orglist_v3.append(
                org.OrganismV2(
                    genome=gns.mutate("AAACCAGAAAAAATTGTAAAAACCGTATTTTAA"),
                    startingLineageName="PT01"))
            alternator += 1
            continue
        if (alternator == 1):
            orglist_v3.append(
                org.OrganismV2(
                    genome=gns.mutate("AGGCCAGAACAAATTGTATTTACAAGGGTCTAA"),
                    startingLineageName="CTS"))
            alternator += 1
            continue
        if (alternator == 2):
            orglist_v3.append(
                org.OrganismV2(
                    genome=gns.mutate("TTTCCAGAACAAATTGTATTTACAAGGGTCTAA"),
                    startingLineageName="CTS"))
            alternator += 1
            continue
        if (alternator == 3):
            orglist_v3.append(
                org.OrganismV2(
                    genome=gns.mutate("AAACCAGAAAAAATTGTAAAAACCGTATTTTAA"),
                    startingLineageName="PT02"))
            alternator += 1
            continue
        if (alternator == 4):
            orglist_v3.append(
                org.OrganismV2(
                    genome=gns.mutate("AAACCAGAAAAAATTGTAAAAACCGTATTTTAA"),
                    startingLineageName="PT03"))
            alternator += 1
            continue
        if (alternator == 5):
            orglist_v3.append(
                org.OrganismV2(
                    genome=gns.mutate("AAACCAGAACAAATTGTATTTACAAGGGTCTAA"),
                    startingLineageName="CTA"))
            alternator = 0
            continue
    print(
        "Succeeded with", len(orglist_v3), "organisms created. (" +
        str(orgcount - len(orglist_v3)) + " not viable)")
    return orglist_v3


def lifeturn_v3(olist, iteration, worldenv, total_iters):
    population_titles = []
    population_counts = []

    mrq = None
    i = 0
    natDis = worldenv.doNaturalDisaster()
    worldenv.clouds()
    print("Iter",
          str(iteration + 1) + "/" + str(total_iters), "- Natural Disaster:",
          natDis, "- Sunlight: ", worldenv.turnSun)
    print("Loading... ", end="")
    lastLength = 0
    for ent in olist:

        if ent.dieOnTurn:
            olist.pop(i)
            continue

        if ent.energy <= 0:
            olist.pop(i)
            continue

        if ent.age > 20:
            olist.pop(i)
            continue

        if natDis and worldenv.natDisasterSeverity > random.randrange(0, 10):
            olist.pop(i)
            continue

        choice = ent.turn(mrq)

        if choice == 1:
            if ent.sex > 0:
                olist.append(
                    org.OrganismV2(genome=gns.mutate(
                        gns.mix(ent.genome, mrq.genome)),
                                   startingLineageName=mrq.sln))
            else:
                olist.append(
                    org.OrganismV2(genome=gns.mutate(ent.genome),
                                   startingLineageName=ent.sln))
        if choice == 2:
            mrq = ent
        if choice == 3:
            i2 = 0
            for y in olist:
                if (y.defense > ent.eatingSkill):
                    i2 += 1
                    continue
                else:
                    ent.energy += y.energy - 1
                    olist.pop(i2)
                    break
        if choice == 4:
            if random.randrange(0, 63) < (worldenv.sunlight /
                                          10) * ent.photosynthesis_effectivity:
                ent.energy += math.round_up(ent.photosynthesis_effectivity /
                                            31.5)

        if ent.lineage in population_titles:
            population_counts[population_titles.index(ent.lineage)] += 1
        else:
            population_titles.append(ent.lineage)
            population_counts.append(1)

        i += 1

        print("\b" * lastLength, end="")
        print(str(i) + "/" + str(len(olist)), end="")
        lastLength = len(str(i) + "/" + str(len(olist)))

    sorted_population_titles = [
        x for _, x in sorted(zip(population_counts, population_titles))
    ]
    print(
        "\nTop Lineage:",
        sorted_population_titles[len(sorted_population_titles) - 1],
        "(" + str(population_counts[population_titles.index(
            sorted_population_titles[len(sorted_population_titles) - 1])]) +
        ")")


def lifeturn_v2(olist, iteration):
    population_titles = []
    population_counts = []

    mrq = None
    i = 0
    for ent in olist:
        if ent.dieOnTurn:
            olist.pop(i)
            continue

        if ent.energy <= 0:
            olist.pop(i)
            continue

        if ent.age > 20:
            olist.pop(i)
            continue

        choice = ent.turn(mrq)

        if choice == 1:
            if ent.sex > 0:
                olist.append(
                    org.OrganismV2(genome=gns.mutate(
                        gns.mix(ent.genome, mrq.genome)),
                                   startingLineageName=mrq.sln))
            else:
                olist.append(
                    org.OrganismV2(genome=gns.mutate(ent.genome),
                                   startingLineageName=ent.sln))
        if choice == 2:
            mrq = ent
        if choice == 3:
            for y in olist:
                if (y.defense > ent.eatingSkill):
                    continue
                else:
                    ent.energy += 7
                    break
        if choice == 4:
            if random.randrange(0, 63) < ent.photosynthesis_effectivity:
                ent.energy += math.round_up(ent.photosynthesis_effectivity /
                                            31.5)

        if ent.lineage in population_titles:
            population_counts[population_titles.index(ent.lineage)] += 1
        else:
            population_titles.append(ent.lineage)
            population_counts.append(1)

        i += 1
    i = 0
    print("ITERATION", iteration, "--------------------------------")
    for x in population_titles:
        print(x + ":", population_counts[i])
        i += 1


def lifeturn(orglist):
    '''A turn in a life, with an organism list. '''
    # Start varriable declaration
    new = 0
    dead = 0
    newR = 0
    p2mrq = None

    C2 = 0
    C1 = 0
    P = 0
    D = 0

    ocne = 0  # DEBUG VAR
    oceat = 0  # DEBUG VAR

    iter = 0
    eatNext_Producer_PrimaryConsuer_DEPRECATED = 0
    for entity in orglist:
        if isinstance(entity, org.PrimaryConsumer):
            C1 += 1
            #RKEY generation - Primary

            MKEY = entity.matechance > random.randint(
                0, 63)  # For mating (SHOULD BE UPDATED)

            ECHANCE = int(entity.eatchance *
                          (len(orglist) / len(orglist))) > random.randint(
                              0, 63)  # changed eating to a mutation

            EMULT = int(
                math.clamp((int(entity.eatchance *
                                (len(orglist) / len(orglist))) - 63) / 63, 0,
                           2))
            #ECHANCE and EMULT are both fucked. Whatevs, we'll change the whole system soon anyways

            ## PRIMARY CONSUMER ##
            if len(orglist) <= 0:
                ECHANCE = False

            entity.turn(MKEY, ECHANCE)

            # Mating - Primary
            if entity.madeKids:
                orglist.append(
                    org.PrimaryConsumer(genome=gns.mutate(entity.genome)))
                new += 1

            # Death checks - Primary
            if entity.energy <= 0:
                orglist.pop(iter)
                dead += 1
                ocne += 1

            if entity.dienextturn:
                oceat += 1  # me thinks this means eaten, but idk
                orglist.pop(iter)

            # Eat checks - Primary
            if ECHANCE:
                eatNext_Producer_PrimaryConsuer_DEPRECATED = 1
                for i2 in range(0, EMULT):
                    eatNext_Producer_PrimaryConsuer_DEPRECATED += 1
                dead += 1 + EMULT

        ## SECONDARY ##

        if isinstance(entity, org.SecondaryConsumer):
            C2 += 1
            if p2mrq == None:  # If no mates, enter -1 attract so nothing happens
                turnchoice = entity.turn(-1, -1)
            if isinstance(p2mrq, org.SecondaryConsumer):
                # if there are things looking to do the wack then do it i guess
                turnchoice = entity.turn(p2mrq.attractiveness, p2mrq.sex)

            # kill the crusty boomers
            if entity.age > 20:
                orglist.pop(iter)
                dead += 1
                iter += 1
                continue

            if entity.dienextturn:
                orglist.pop(iter)
                dead += 1
                iter += 1
                continue

            # Creature accepts one-night-stand request and makes a mistake that turns out to be alive
            if turnchoice == 1:
                if random.randrange(0, 3) == 2:
                    orglist.append(
                        org.SecondaryConsumer(age=0,
                                              genome=gns.mix(
                                                  gns.mutate(entity.genome),
                                                  gns.mutate(p2mrq.genome))))

                orglist.append(
                    org.SecondaryConsumer(age=0,
                                          genome=gns.mix(
                                              gns.mutate(entity.genome),
                                              gns.mutate(p2mrq.genome))))

                p2mrq = None
            # Creature puts out a one-night-stand request
            if turnchoice == 2:
                p2mrq = entity
            # Kill something because hungri
            if turnchoice == 3:
                for i2 in range(len(orglist)):
                    try:
                        if entity.strength > orglist[i2].defense:
                            entity.energy += 4
                            orglist.pop(i2)
                            dead += 1
                            break
                    except:
                        pass

            if entity.energy < 1:
                orglist.pop(iter)
                dead += 1
                iter += 1
                continue

        # Soil fertiity checks
        soilFert = 0
        soilFert += (dead) // 10  # Dead organisms go here

        # Decomposer turn
        if isinstance(entity, org.Decomposer):
            D += 1
            DKEY = entity.sporechancegen > random.randrange(0, 32)

            #print(len(orglist))
            entity.turn(float(soilFert), DKEY, len(orglist) - D)

            # Mating - Decomposer
            if entity.spread:
                orglist.append(
                    org.Decomposer(genome=gns.mutate(entity.genome)))
            # Soil enrichment - Decomposer

            # Consumption - Decomposer

            # Death - Decomposer
            if entity.energy <= 0:
                dead += 1
                orglist.pop(iter)

        # Resource Life Cycle
        if isinstance(
                entity,
                org.Producer):  #x in rlist is fix to index out of bounds error
            P += 1
            ## PLANT LIFE TURN
            SEED_KEY = (entity.seedchance + soilFert) - (P) > random.randint(
                0, 64)
            #seed key is fucked after refactor, too bad it won't exist for long :P

            entity.turn()  # Turn

            # Mating - Resource
            if (entity.age > 2) and SEED_KEY:
                orglist.append(org.Producer(genome=gns.mutate(entity.genome)))
                newR += 1

            # Old Age - Resource
            if entity.age > 5:
                orglist.pop(iter)

        iter += 1
    """
  print('There are ', len(plist), ' primary consumers in the simulation.')
  print(dead, ' primary consumers have died. ')
  print(new, ' primary consumers have been born.')
  print("The average eating skill of all consumers this round was " +
        str(averageEatChance))
  print('\n')
  print('There are ', len(rlist), ' resources in the simulation.')
  print(dead, ' resources have died.')
  print(newR, ' resources have grown.')"""
    if debugData == True:
        print("1CN:", new, "1CD(ne): ", ocne)
    print("2C:", C2, "1C:", C1, "D:", D, "P:", P)


#This is a variable so it's easy to see and edit, and reusable easily

#This is a variable so it's easy to see and edit, and reusable easily

#Wtf are those two comments


def lifeturnAll(orglist, iteration, ver, worldenv, totalIterations):
    if ver == 1:
        lifeturn(orglist)
    elif ver == 2:
        lifeturn_v2(orglist, iteration)
    else:
        exec("lifeturn_v" + str(ver) +
             "(orglist, iteration, worldenv, totalIterations)")


def startCivFL(FL):
    #This shit should actually be on the unforgivable crime. I tried using execs but it wouldn't return, so we're stuck with this.
    if FL == 1:
        print("Organism FL1 is not supported by any current lifeturn version.")
    if FL == 2:
        return startCiv_v2()
    if FL == 3:
        return startCiv_v3()


def createWorldEnvFL(fl):
    if (fl == -1) or (fl == "X"):
        return None
    else:
        sun = int(input("How effective should photosynthesis be? (0-10)\n> "))
        ndor = int(
            input(
                "What should the chance of a natural disaster be?(1 in x chance of occurence)\n> "
            ))
        nds = int(
            input("How severe should the natural disasters be? (0-10)\n> "))
        return env.WorldEnvironment(sun, ndor, nds)


compatibility = """Compatible versions:
Lifeturn V1 - Organism FL2
Lifeturn V2 - Organism FL3
Lifeturn A3 - Organism FL3 - WorldEnv A0"""

organismFL = 3
lifeturnVer = 2
worldEnv = "X"

print(compatibility)
otk = input("Enter OtherTest Key (press enter if none)\n> ")
if otk == "20S":
    tS.init_20S()
if otk == "16D":
    sD.init_16d()

global debugData
debugData = False
organismFL = int(
    input("Organism feature level (latest: 3, recommended: 2)\n> "))
lifeturnVer = int(
    input("Lifeturn feature level (latest: 3, recommended: 1)\n> "))
if organismFL == 2 and lifeturnVer == 1:
    if input(
            "Would you like debug prints (for 2,1 only, NOT RECOMENDED)('yes' for confirmation)\n> "
    ) == 'yes':
        debugData = True
    else:
        debugData = False
if (lifeturnVer >= 3):
    worldEnvVer = int(input("World Environment feature level (latest: 0)\n> "))
else:
    worldEnvVer = -1

if (lifeturnVer == 1
        and organismFL != 2) or (lifeturnVer == 2 and organismFL < 3) or (
            lifeturnVer > 3) or (organismFL > 3) or (worldEnvVer > 0):
    print("Selected OFL/Lifeturn/WorldEnv combination is not compatible!")
    print(compatibility)
    exit()

if (worldEnvVer == -1):
    worldEnvVer = "X"

print("Life Simulator v" + str(organismFL) + str(lifeturnVer) +
      str(worldEnvVer))
#v32X denotes Feature Level 3 organisms/list type, lifeturn version 2, and X level environment (nonexistent)
#Note that no code is technically deprecated. This is on purpose because LifeForage should be very customizable.

print("Generating organism start list with feature level " + str(organismFL) +
      "...")
orglist = startCivFL(organismFL)
worldenv = createWorldEnvFL(worldEnvVer)
print("Done!")
print("Using lifeturn version " + str(lifeturnVer) + ".")
if isinstance(worldenv, env.WorldEnvironment):
    print("WorldEnv:", worldenv.sunlight, worldenv.natDisasterOccuranceRate,
          worldenv.natDisasterSeverity)
else:
    print("No WorldEnv.")


def start():
    a = int(input('How many simulation cycles?\n> '))
    for i in range(a):
        #Actuall code thats running the entire thing
        #^^^^ OG comment, do not remove ^^^^

        lifeturnAll(orglist, i, lifeturnVer, worldenv, a)
    print('')  # EEEEEWWWWWW haha lol
    start()


if __name__ == "__main__":
    start()
