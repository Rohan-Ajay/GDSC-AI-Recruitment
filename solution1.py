# -*- coding: utf-8 -*-
"""Solution1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_gz88f1OdpgsOznbKih_fT1T-wJEDap9

**GDSC AI/ML Challenge**
"""

def StringManipulation(Str):
  L=list(Str)

  # Replacing String with succeeding alphabets, numbers undisturbed
  for k in L:
    if k=='z':
      L[L.index(k)]='a'
    if k=='Z':
      L[L.index(k)]='A'
    if k.isalpha()==False:
      continue
    if (k!='Z' and k!='z'):
      y=ord(k)
      L[L.index(k)]=chr(y+1)
  string1=''.join(map(str,L))
  print()
  print("Replacing String with succeeding alphabets, numbers undisturbed :")
  print(string1)

  # Removing all vowels and inverting the string
  s=list(Str)
  for k in s:
    if k in'AEIOUaeiou':
      s.pop(s.index(k))
  n=s[::-1]
  string2=''.join(map(str,n))
  print()
  print("Removing all vowels and inverting the string :")
  print(string2)

  # Printing every alternate character from the original string
  print()
  print("Printing every alternate character from the original string :")
  print(Str[0:len(Str)+1:2])

Str=input('Enter string : ')
StringManipulation(Str)