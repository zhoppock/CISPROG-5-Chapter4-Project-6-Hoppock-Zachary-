def decimalToBinary(number):
  decimal = int(number)
  if decimal == 0:
    print(0)
  else:
    print("\nQuotient Remainder Binary")
    bitString = ""
    while decimal > 0:
      remainder = decimal % 2
      decimal = decimal // 2
      bitString = str(remainder) + bitString
      print("%5d%8d%12s"% (decimal, remainder, bitString))
  print("The binary value is", bitString)
  return bitString