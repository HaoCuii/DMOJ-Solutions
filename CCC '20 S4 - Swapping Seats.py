import sys
s = list(sys.stdin.readline().strip())
min_swaps = float('inf')
l = len(s)

psa_a,psa_b,psa_c = [0]*(l*2),[0]*(l*2),[0]*(l*2)
for i in range(l):
    psa_a[i],psa_b[i],psa_c[i] = psa_a[i-1],psa_b[i-1],psa_c[i-1]
    if s[i] == 'A':
        psa_a[i] += 1
    elif s[i] == 'B':
        psa_b[i] += 1
    else:
        psa_c[i] += 1
for i in range(l,l*2):
    psa_a[i],psa_b[i],psa_c[i] = psa_a[i-1],psa_b[i-1],psa_c[i-1]
    if s[i-l] == 'A':
        psa_a[i] += 1
    elif s[i-l] == 'B':
        psa_b[i] += 1
    else:
        psa_c[i] += 1 

ca,cb,cc = psa_a[l-1],psa_b[l-1],psa_c[l-1]
def swaps(b,cb,i):
    na = ca - psa_a[i+ca] + psa_a[i]
    nb = cb - b[i+ca+cb] + b[i+ca]
    S = min(psa_a[i+ca+cb] - psa_a[i+ca],b[i+ca] - b[i])
    return na+nb-S

for i in range(l):
    min_swaps = min(swaps(psa_b,cb,i),min_swaps)
    min_swaps = min(swaps(psa_c,cc,i),min_swaps)


print(min_swaps)







