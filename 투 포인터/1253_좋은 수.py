import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int,input().split()))

result = 0

A.sort()

for k in range(N):
    find = A[k]
    i = 0
    j = N-1
    while i < j :
        if A[i] + A[j] == find:
            if i != k and j != k :
                result += 1
                break
            # 자기 자신을 더해서 만든 셈이 되기 때문에 이를 건너뜀
            elif i == k :
                i += 1
            elif j == k :
                j -= 1
        elif A[i] + A[j] > find:
            j -= 1

        else :
            i += 1

print(result)