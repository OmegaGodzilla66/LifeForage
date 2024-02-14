# An easy way to create genomes: Run this file to create your own genome
import imp.genetics as gns

print("Put in numbers, type STOP1 (TAA), STOP2 (TGA), or STOP3 (TAG) to add stop codon, type START1 (ATG), START2 (TTG), or START3 (GTG) to add start codon and any single letter is end.")
inp = 0
inp_raw = ""
sbuild = ""
while True:
  inp_raw = input("> ")
  if (inp_raw == "STOP1"):
    sbuild += "TAA"
    continue
  if (inp_raw == "STOP2"):
    sbuild += "TGA"
    continue
  if (inp_raw == "STOP3"):
    sbuild += "TAG"
    continue
  #somebody tell ethan that there is only ONE START CODON - jacob no
  if (inp_raw == "START1"):
    sbuild += "ATG"
    continue
  if (inp_raw == "START2"):
    sbuild += "TTG"
    continue
  if (inp_raw == "START3"):
    sbuild += "GTG"
    continue
  try:
    inp = int(inp_raw)
    sbuild += gns.b10_b4_codon(inp)
  except:
    break
print("Out: " + sbuild)
