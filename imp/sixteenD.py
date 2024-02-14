import random
import imp.genetics as gns

# Test environment 16D
# Purpose: Testing Importance of Food vs. Mating in a two-organism Environment


# Organism A: Food Gathering
# Organism B: Mating

# WorldEnv: PlantGenome

class Organism16D:
    # GENOME KEY
    # Hunting Skill, Mating Skill STOP
    def __init__(self,genome,lineage):
        self.genome=genome
        self.lineage=lineage
        self.age=0
        self.eats=False # this is done as an inevitable solution to the crisis of not enough food
        self.decGenome=gns.decode(genome)
        self.todie=False
        self.tomate=False
        
        self.energy=2

    def turn(self):
        self.age+=1
        if self.age>8:
            self.energy-=1
        if self.age>10:
            self.energy-=1


        self.energy-=1 # The circle of life

    def __eq__(self, other):
        """returns if this is equal to another's sight genome thing"""
        return self.decGenome[1] == other.decGenome[1]

    def __lt__(self, other):
        """returns if this is less than another's sight genome thing"""
        return self.decGenome[1] < other.decGenome[1]

        


class WorldEnv16D:
    def __init__(self):
        self.plants=2000

def startCiv16D(numA, numB):
    orgList=[]
    for i in range(numA):
        # 60, 10
        orgList.append(Organism16D(gns.mutate("TATAGGTAA"),"A")) # Type A: Starts with HuntPreference
    for i in range(numB):
        # 10, 60
        orgList.append(Organism16D(gns.mutate("AGGTATTAA"),"B")) # Type B: Starts with MatePreference

    return orgList

def lifeturn16D(orglistUNSORT,we,printType):
    # Organism
    orglist = sorted(orglistUNSORT)
    for i in range(len(orglist)):
        # Mate
        if orglist[i].age>7 and orglist[i].energy>5:
            MKEY=random.randrange(0,63)
            if MKEY>orglist[i].decGenome[1]:
                orglist[i].tomate=True
                orglist[i].energy-=7
        # Life Energy Tax
        orglist[i].turn()
        if orglist[i].energy<=0:
            orglist[i].todie=True

        # Eat
        if we.plants==0:
            eatKEY=0
        else:
            eatKEY=random.randrange(0,87)

        if orglist[i].decGenome[0]+eatKEY>=75:
            orglist[i].energy+=3
        else:
            pass # hungrrrrrrrrr

        # Mate
    
            
    iter=0
    for entity in orglist:
        if entity.todie:
            orglist.pop(iter)
        if entity.tomate:
            orglist.append(Organism16D(gns.mutate(entity.genome),entity.lineage))
        iter+=1
    if printType==1:
        for i in range(len(orglist)):
            print(f"""ORGANISM ITER: {i} Lineage: {orglist[i].lineage} Genome: {orglist[i].genome} Energy: {orglist[i].energy}""")

    
    
    # end organism

    # WorldEnv
    we.plants*=1.5
    we.plants+=10
    return orglist

def init_16d():
    print("""# Simulation 20D #
    Purpose: Testing Contrast in Features in a Two-Organism Environment
    Features: Hunting Strength, Mating
    WorldEnv: Plants
    Inputs Required: 2 type:int for Organism Populations. 
    Organism is a SINGLE CLASS, and uses the same genome interpretation for each lineae.
    NO ADDITIONAL SOFTWARE IS REQUIRED FOR THIS OTHERTEST
    The mutation level for this environment is HIGH. 50% CHANCE FOR ORGANISM TO MUTATE""")
    orglist=startCiv16D(int(input("Enter Number of Type A Organisms\n> ")), int(input("Enter Number of Type B Organisms\n> ")))
    print("""Please select your print type (defaults to printtype2):
    [1]: Print Type A: Prints the genome, lineage, and feature interpretations for each organism
    [2]: Print Type B: Prints the average stats for each feature for each lineage""")
    if input("> ")=="1":
        printType=1
    else:
        printType=2
    we=WorldEnv16D()
    while len(orglist)>0:
        print("-----START OF ITERATION-------")
        orglist=lifeturn16D(orglist,we,printType)
        print("-----FINISHED ITERATION-------")
        if printType==2:
            lineageACount=0
            lineageBCount=0
            lineageAEnergyAverage=0
            lineageBEnergyAverage=0
            lineageABestEatStat=0
            lineageBBestEatStat=0
            lineageABestMateStat=0
            lineageBBestMateStat=0
            for i in range(len(orglist)):
                entity=orglist[i]
                if entity.lineage=="A":
                    lineageACount+=1
                    lineageAEnergyAverage+=entity.energy
                    if lineageABestEatStat<entity.decGenome[0]:
                        lineageABestEatStat=entity.decGenome[0]
                    if lineageABestMateStat<entity.decGenome[1]:
                        lineageABestMateStat=entity.decGenome[1]
                elif entity.lineage=="B":
                    lineageBCount+=1
                    lineageBEnergyAverage+=entity.energy
                    if lineageBBestEatStat<entity.decGenome[0]:
                        lineageBBestEatStat=entity.decGenome[0]
                    if lineageBBestMateStat<entity.decGenome[1]:
                        lineageBBestMateStat=entity.decGenome[1]
                else:
                    raise "Invalid Lineage - Organism lineage not A or B"
            print(f"""Stats Per Lineage:""")
            if lineageACount==0:
                print("    Lineage A: \n\t\tDECEASED. ")
            else:
                print(f"""    Lineage A: 
        Population: {lineageACount}
        Energy Average: {lineageAEnergyAverage/lineageACount}
        Best Eat Stat: {lineageABestEatStat}
        Best Mate Stat: {lineageABestMateStat}""")
            print("    - - - - - - - - - - - - - - -")
            if lineageBCount==0:
                print("    Lineage B: \n\t\tDECEASED. ")
            else:
                print(f"""
    Lineage B:
        Population: {lineageBCount}
        Energy Average: {lineageBEnergyAverage/lineageBCount}
        Best Eat Stat: {lineageBBestEatStat}
        Best Mate Stat: {lineageBBestMateStat}""")
        
        
        print(f"Total Organisms: {len(orglist)}")
        input("Press enter to continue\n> ")
        global geneMutFactor
        print(GENE_MUT_FACTOR)
    print("Number of Organisms has reached 0")
    exit()
