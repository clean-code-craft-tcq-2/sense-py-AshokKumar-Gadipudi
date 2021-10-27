from statistics import mean

def calculateStats(numbers,counter):

  if counter == 0:
    return mean(numbers)
  elif counter == 1:
    return max(numbers)
  elif counter == 2:
    return min(numbers)
