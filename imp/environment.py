import random

class WorldEnvironment:
  '''Basic world gen stuff - NOT USED IN NON-BETA VERSIONS OF LIFETURN'''
  def __init__(self, sunlight=10, natDisasterOccuranceRate=100, natDisasterSeverity=5):
    self.sunlight = sunlight
    self.turnSun=sunlight
    self.natDisasterOccuranceRate = natDisasterOccuranceRate
    self.natDisasterSeverity = natDisasterSeverity

  def doNaturalDisaster(self):
    if random.randint(1, self.natDisasterOccuranceRate) == random.randint(1, self.natDisasterOccuranceRate):
      return True
    return False

  def clouds(self):
    CloudKEY=random.randint(-20,20)/5
    self.turnSun=self.sunlight+CloudKEY
