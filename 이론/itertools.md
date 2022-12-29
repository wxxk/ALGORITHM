### itertools

> 효율적인 루핑을 위한 이터레이터를 만드는 함수



**[조합형 이터레이터]**

| 이터레이터                      | 인자                 | 결과                                                |
| ------------------------------- | -------------------- | --------------------------------------------------- |
| product()                       | p, q, ... [repeat=1] | 데카르트의 곱, 중첩된 for 루프와 동등               |
| permutations()                  | p[, r]               | r-길이 튜플들, 모든 가능한 순서, 반복되는 요소 없음 |
| combinations()                  | p, r                 | r-길이 튜플들, 정렬된 순서, 반복되는 요소 없음      |
| combinations_with_replacement() | p, r                 | r-길이 튜플들, 정렬된 순서 반복되는 요소 있음       |

| 예                                       | 결과                                            |
| ---------------------------------------- | ----------------------------------------------- |
| product('ABCD', repeat=2)                | AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD |
| permutations('ABCD', 2)                  | AB AC AD BA BC BD CA CB CD DA DB DC             |
| combinations('ABCD', 2)                  | AB AC AD BC BD CD                               |
| combinations_with_replacement('ABCD', 2) | AA AB AC AD BB BC BD CC CD DD                   |



```python
# product(*iterables, repeat=1) : 여러 iterable의 데카르트곱 리턴
# product는 다른 함수와 달리 인자로 여러 iterable을 넣어줄 수 있고 그 친구들간의 모든 짝을 지어서 리턴합니다.

from itertools import product

l1 = ['A', 'B']
l2 = ['1', '2']

for i in product(l1, l2, repeat=1): # l1과 l2의 모든 쌍을 지어 리턴한다.
    print(i)
    
'''
출력결과:
('A', '1')
('A', '2')
('B', '1')
('B', '2')
'''

for i in product(l1, repeat=3): # product(l1, l1, l1, repeat=1)과 동일한 출력
    print(i)

'''
출력결과:
('A', 'A', 'A')
('A', 'A', 'B')
('A', 'B', 'A')
('A', 'B', 'B')
('B', 'A', 'A')
('B', 'A', 'B')
('B', 'B', 'A')
('B', 'B', 'B')
'''
```



```python
# permutations(iterable,r=None) : iterable에서 원소 개수가 r개인 순열 뽑기

'''
순열
서로 다른 n개중에 r개를 선택하는 경우의 수(순서 상관 있음)
'''

from itertools import permutations

l = ['A', 'B', 'C']

for i in permutations(l): # r을 지정하지 않거나 r=None으로 하면 최대 길이의 순열이 리턴된다.
    print(i)
    
'''
출력결과:
('A', 'B', 'C')
('A', 'C', 'B')
('B', 'A', 'C')
('B', 'C', 'A')
('C', 'A', 'B')
('C', 'B', 'A')
'''
```



```python
# combinations(iterable, r) : iterable에서 원소 개수가 r개인 조합 뽑기

'''
조합
서로 다른 n개중에 r개를 선택하는 경우의 수(순서 상관 없음)
'''

from itertools import combinations

l = [1, 2, 3]

for i in combinations(l,2):
    print(i)
    
'''
출력 결과:
(1, 2)
(1, 3)
(2, 3)
'''
```



```python
# combinations_with_replacement(iterable,r) : iterable에서 원소 개수가 r개인 중복 조합 뽑기

'''
중복순열
중복 가능한 n개중에서 r개를 선택하는 경우의 수
'''

from itertools import combinations_with_replacement

l = ['A', 'B', 'C']

for i in combinations_with_replacement(l,2):
    print(i)
    
'''
출력결과:
('A', 'A')
('A', 'B')
('A', 'C')
('B', 'B')
('B', 'C')
('C', 'C')
'''
```

