import random
import math
from random_better import get_next_base4rands
    
GENE_MUT_FACTOR = 1 # chance for a letter to mutate is 1/GENE_MUT_FACTOR
GENE_MUT_FACTOR = math.ceil((math.log2(GENE_MUT_FACTOR)/math.log2(4))+0.5) # comment this if going back to old random

def split3s(input):
    i = 0
    sb = ""
    lb = []
    for x in input:
        sb += x
        if i != 2: i += 1
        else:
            i = 0
            lb.append(sb)
            sb = ""
    return lb


def codon_b4_b10(codon):
    '''Parses a codon into readable numbers transfered into features'''
    parsed = codon.replace("A", 
                           "0").replace("C",
                                        "1").replace("G",
                                                     "2").replace("T", "3")
    #^why
    return (int(parsed[0]) * 16) + (int(parsed[1]) * 4) + int(parsed[2])


def b10_b4_codon(num):
    '''Parses a base 10 number into a codon'''
    prcs = num
    x = 64
    outb4 = ""
    while len(outb4) < 3:
        x = int(prcs % 4)
        prcs = (prcs - (x)) / 4
        outb4 = str(x) + outb4
    return outb4.replace("0", "A").replace("1",
                                             "C").replace("2",
                                                          "G").replace("3", "T")


def decode(gene):
  '''Decode codons into list of integers'''
  valid = True
  if isinstance(gene, str):
    for char in gene:
      if not (char == "A" or char == "C" or char == "G" or char == "T"):
        valid = False
  if not valid: return
  codons = split3s(gene)
  out = []
  enabled = True
  for x in codons:
    if x == "TAA" or x == "TAG" or x == "TGA":
      enabled = False
    if enabled:
      out.append(codon_b4_b10(x))
    if not enabled and (x == "ATG" or x == "TTG" or x == "GTG"):
      enabled = True
  return out

# this is such a stupid function
def check_if_not_3(number):
    match number:
        case 3:
            return False
        case _:
            return True

def _mutate(gene):
    global GENE_MUT_FACTOR
    '''Mutate genome'''
    #a = ""
    gene_new = gene
    mutate = False
    rands = get_next_base4rands((len(gene))*4)
    randgenes = get_next_base4rands(len(gene))
    loc = -1
    for n in range(len(gene)):
        for m in range(GENE_MUT_FACTOR):
            loc += 1
            if rands[loc] == 3 :
                mutate = True
                pass
            else : break
            #match rands[(n*GENE_MUT_FACTOR)+m]:
            #    case 3:
            #        mutate = True
            #        pass
            #    case _:
            #        break
        if mutate:
            gene_new[n] = randgenes[n]
    return gene_new
    #for x in gene:
        #if random.randint(0, int(960 / len(gene))) == random.randint(0, int(960 / len(gene))):
        #    b = random.randint(0, 3)
        #    if b == 0:
        #        a += "A"
        #    if b == 1:
        #        a += "C"
        #    if b == 2:
        #        a += "G"
        #    if b == 3:
        #        a += "T"
        #else:
        #    a += x
    #return a
def mutate(gene):
    '''Mutate genome'''
    a = ""
    for x in gene:
        if random.randint(0, int(960 / len(gene))) == random.randint(0, int(960 / len(gene))):
            b = random.randint(0, 3)
            if b == 0:
                a += "A"
            if b == 1:
                a += "C"
            if b == 2:
                a += "G"
            if b == 3:
                a += "T"
        else:
            a += x
    return a
def mix(genome1, genome2):
    """Mix genome of 2 organisms (sexual reproduction)"""
    a = ""
    for i in range(len(genome1)):
        if (genome1[i] == genome2[i]):
            a += genome1[i]
        elif random.randint(0, 1) == 1:
            a += genome1[i]
        else:
            a += genome2[i]
    return a


if (__name__ == "__main__"):
    print("GENETICS MODULE SELF TEST - V23W10A")
    print("ACTTAAGTC")
    print("DECODED:", decode("ACTTAAGTC"))
    print("7")
    print("ENCODED:", b10_b4_codon(7))
