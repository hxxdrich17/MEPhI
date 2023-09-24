import math

k = [3.421, 3.487, 4.6, 4.263, 4.123, 4.037]

sigm = 0
k_s = 0

k_s = sum(k)/len(k)

for i in range(len(k)):
    sigm += (k[i] - k_s)**2
    
sr_otkl = 0.19
# math.sqrt(  sigm/(len(k)*(len(k) - 1)) )

g = (4 * math.pi**2)/ k_s
delta_g = (4 * math.pi**2 * sr_otkl)/ (k_s**2)

print(f"<k>: {k_s}\npogr: {sr_otkl}\ng: {g} +- {delta_g}")