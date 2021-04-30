#Importing numpy, scipy, mpmath and pyplot
import numpy as np
import matplotlib.pyplot as plt
import math
import scipy
import scipy.stats as ss
#if using termux
import subprocess
import shlex
#end if

a=0
b=0
c=0
d=0
e=0
rand=[]
#simulation
simlen = int(1e6)
for i in range(0,10):
  rand.append(np.random.normal(0,1,simlen))

for i in range(0,simlen):
  sum=0
  for j in range(1,10):
    sum=sum+rand[j][i]
  if rand[0][i]>sum:
    a=a+1
print(a/simlen)
#print(rand,rand[2][1])
for i in range(0,simlen):
  prod=1
  for j in range(1,10):
    prod=prod*rand[j][i]
  if rand[0][i]>prod:
    b=b+1
print(b/simlen)

for i in range(0,simlen):
  sum=0
  for j in range(1,10):
    sum=sum+math.sin(rand[j][i])
  if math.sin(rand[0][i])>sum:
    c=c+1
print(c/simlen)

for i in range(0,simlen):
  sum=0
  for j in range(1,10):
    sum=sum+rand[j][i]
  if math.sin(rand[0][i])>math.sin(sum):
    d=d+1
print(d/simlen)

###test###
for i in range(0,simlen):
  sum=0
  for j in range(1,10):
    sum=sum+math.sin(rand[j][i])+(rand[j][i])**3
  if (math.sin(rand[0][i])+(rand[0][i])**3) >sum:
    e=e+1
print(e/simlen)