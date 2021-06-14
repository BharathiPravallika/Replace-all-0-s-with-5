def convertFive(n):
  arr = [int(x) for x in str(n)]
  res = [5 if x == 0 else x for x in arr]
  
  s = "".join(map(str, res))
  return int(s)

print(convertFive(int(input("enter your number:\n").strip())))
