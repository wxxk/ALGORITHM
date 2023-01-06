# sys.setrecursionlimit()

파이썬으로 재귀를 사용해 문제를 풀 때 특히, DFS, BFS 문제를 풀 때 예시에서 답은 잘 나오는데, 정답을 제출을 하면 런타임 에러를 접하게 되는 경우가 있다.

대부분 파이썬의 재귀 최대 깊이의 기본 설정이 1,000회 이기 때문에 런타임 에러가 발생하는 경우이다.

이런 문제를 해결하기 위해서는 아래와 같이 코드를 작성해주면 됩니다.

```python
import sys
sys.setrecursionlimit(10 ** 6)
```

위와 같이 코드의 상단에 `sys.setrecursionlimit(10**6)`을 작성해주면 재귀의 최대 깊이가 10**6으로 바뀌게 된다.

유의해야할 점은 `PyPy`에서는 `sys.setrecursionlimit()`으로 임의로 재귀의 최대 깊이를 설정할 수 없다는 점이다.

파이썬으로 코딩 테스트를 준비한다면 sys 라이브러리는 `sys.stdin.readline()`, `sys,setrecursionlimit()` 등 유용하게 활용할 수 있으니 평소에 많이 익숙해질 수 있도록 해야한다.