import sys

sys.stdin = open("input.txt")
sys.stdin.readline

n = int(input())
tree = dict()

# 반복문을 통해 트리 생성
for i in range(n):
    root, left, right = map(str, input().split())
    tree[root] = left, right


# 전위 순회
def preorder(v):
    if v != ".":  # 자식이 있다면
        print(v, end="")  # 루트 자식 노트 출력
        preorder(tree[v][0])  # 재귀적으로 왼쪽 노드 탐색
        preorder(tree[v][1])  # 재귀적으로 오른쪽 노드 탐색


# 중위 순회
def inorder(v):
    if v != ".":  # 자식이 있다면
        inorder(tree[v][0])  # 재귀적으로 왼쪽 노드 탐색
        print(v, end="")  # 루트 노드 출력
        inorder(tree[v][1])  # 재귀적으로 오른쪽 노드 탐색


# 후위 순회
def postorder(v):
    if v != ".":  # 자식이 있다면
        postorder(tree[v][0])  # 재귀적으로 왼쪽 노드 탐색
        postorder(tree[v][1])  # 재귀적으로 오른쪽 노드 탐색
        print(v, end="")  # 루트 노드 출력


preorder("A")
print()
inorder("A")
print()
postorder("A")
