#https://codeforces.com/problemset/problem/158/A
while True:
    n, k = map(int, input().split())
    if (n <= 50)and (k >= 1) and (n >= k) :
        break
arr = [int(x) for x in input().split()]
next_round = [x for x in arr if (x > 0 and x >= arr[k - 1])]
print(len(next_round))