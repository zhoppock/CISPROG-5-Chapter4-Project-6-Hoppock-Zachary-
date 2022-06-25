def encryption(number):
  print("\nYour plaintext is:", number)
  plainText = number
  distance = 1
  code = ""
  for ch in plainText:
    ordvalue = ord(ch)
    cipherValue = ordvalue + distance
    if cipherValue > ord('9'):
      cipherValue = ord('0') + distance - (ord('9') - ordvalue + 1)
    code += chr(cipherValue)
  print("The encrypted number is:", code)
  return code