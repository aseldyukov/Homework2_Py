# function that counts the number of sheep present in the array (true means present)
def count_sheeps(arrayOfSheeps):
  Sheeps = 0
  for i in arrayOfSheeps:
      if i == True:
          Sheeps += 1
  return Sheeps