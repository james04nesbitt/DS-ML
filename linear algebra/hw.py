import math
import numpy
pi = math.pi
c1 = math.cos((94*pi)/365)
c2 = math.cos((148*pi)/365)
c3 = math.cos((181*pi)/365)

s1 = math.sin((94*pi)/365)
s2 = math.sin((148*pi)/365)
s3 = math.sin((181*pi)/365)

k1 = (s2-s1)/(c2-c1)
k2 = 0.5/(c2-c1)

c = ((0.5)/(c3-c1)-k2)/((s3-s1)/(c3-c1)-k1)
print(c)


