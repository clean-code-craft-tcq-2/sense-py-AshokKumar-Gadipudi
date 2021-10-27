variable = 0

def calculateStats(numbers,counter):

  variable = counter
  if variable == 0:
    return sum(numbers) / len(numbers)
  elif variable == 1:
    return max(numbers)
  elif variable == 2:
    return min(numbers)
