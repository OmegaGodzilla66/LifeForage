import math


def clamp(num, min_value, max_value):
  return max(min(num, max_value), min_value) #why no included in included math.py

def round_up(num):
  return math.ceil(num) #because for some reason, importing this and the other math doesn't work
