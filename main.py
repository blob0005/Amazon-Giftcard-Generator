import random
import time
try:
    import os
    from os import system
    system("title " + "Amazon Giftcard Generator,   Made By blob#0005,   Github: github.com/blob0005")
except:
    pass
while True:
  save = input("Wanna Auto Save (y/n): ")
  if save == "y" or save == "n":
    break
  else:
    print("Enter A Valid Choice")
while True:
  try:
    amount = input("Amount Of Codes: ")
    amount = int(amount)
    break
  except Exception:
    print("Enter A Valid Choice")
while True:
  try:
    delay = input("Delay: ")
    delay = float(delay)
    break
  except Exception:
    print("Enter A Valid Choice")
donegen = 0
choices = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
for i in range(int(amount)):
  r1 = random.choices(choices, k=14)
  code = "".join(r1)
  if save == "y":
    file = open("unchecked_amazon_codes.txt", "a")
    file.write(code + "\n")
    file.close()
  donegen = int(donegen) + 1
  print("Generated Code: " + str(code) + "     Done With: " + str(donegen))
  time.sleep(float(delay))
print("Done")
input("")
exit()
