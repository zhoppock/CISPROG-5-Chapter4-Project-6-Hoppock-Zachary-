from encryption import encryption
from decimalToBinary import decimalToBinary
from shiftLeft import shiftLeft

decimal = input("Input a decimal integer: ")

code = encryption(decimal)
bitString = decimalToBinary(code)
encryptedNum = shiftLeft(bitString)

print("\nYour encrypted binary number is: " + encryptedNum)