N = int(input())
data = []
for _ in range(N):
    d = int(input())
    data.append(d)

for i in range(N):
    for j in range(N - 1):
        if data[j] < data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]

print(" ".join(map(str, data)))
