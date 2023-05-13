import sys

input = sys.stdin.readline

word = {}
total = 0
while True:
    s = input().strip()
    if not s:
        break
    word[s] = 1 + word.get(s, 0)
    total += 1

word_lst = sorted(list(word.keys()))

for i in word_lst:
    print(f"{i} {(word[i]/total)*100:.4f}")
