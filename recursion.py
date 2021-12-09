# -*- coding: utf-8 -*-


#Part I ­ Implement the Fibonnaci Sequence
def fibonnaci(n):
    if n <= 1:
        return n
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)
    
#Part II ­ Implement Euclid’s GCD Algorithm    
def gcd(a, b):
    if b > a:
        return gcd(b, a)

    if a % b == 0:
        return b
    r = a % b
    return gcd(b, r)   

#Part III ­ String Comparison

def compareTo(s1, s2):
  lens1 = len(s1)
  lens2 = len(s2)
  if lens1 > lens2:
      return  1
  elif lens1< lens2:
      return -1
  else:
      if (s1 and s2) and (s1[0] == s2[0]):
          compareTo(s1[1:], s2[1:])
          return 0
        
    