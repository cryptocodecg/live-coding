# -*- coding: utf-8 -*-
"""ember.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aqNf5taLKb7H4TQyAs5kmwv92SJNprgR
"""

x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

a = 1
while True:
  b = (z - x*a)

  if b % y == 0:
    b = b/y
    print(a, int(b))
    break
  else:
    a = a + 1

x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

solution = False
for a in range(z):
  b = (z - x*a)

  if b % y == 0:
    b = b/y
    print(a, int(b))
    solution = True
    break

if solution == False:
  print("There is no solution")