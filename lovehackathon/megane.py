N = int(input())
NumSequence = sorted(map(int, input().split()), reverse=True)

CenterIndex = (N + 1) // 2 - 1
Answer = NumSequence[CenterIndex]
print(Answer)
