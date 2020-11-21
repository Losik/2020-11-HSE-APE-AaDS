# Skip number of elements
input()

cumulative_sums = [0]
for value in map(int, input().split()):
    cumulative_sums.append(cumulative_sums[-1] + value)

for i in range(int(input())):
    begin, end = map(int, input().split())
    print(cumulative_sums[end] - cumulative_sums[begin - 1])
