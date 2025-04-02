import sys
input = sys.stdin.readline

# N: 재료의 개수
# M : 갑옷이 되는 번호
# A : 정렬된 리스트
N = int(input())
M = int(input())
count = 0
A = list(map(int,input().split()))
A.sort()

i = 0
j = N - 1

while i < j :
    if A[i] + A[j] == M:
        count += 1
        i += 1
        j -= 1

    elif A[i] + A[j] > M:
        j -= 1

    else :
        i += 1

print(count)