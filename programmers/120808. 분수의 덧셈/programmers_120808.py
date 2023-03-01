numer1 = 1
denom1 = 2
numer2 = 3
denom2 = 4

max_denom = max(denom1, denom2)
min_denom = min(denom1, denom2)

temp = max_denom // min_denom

max_numer = max(numer1, numer2)
min_numer = min(numer1, numer2)

answer = [max_numer + (min_numer * temp), max_denom]
print(answer)
