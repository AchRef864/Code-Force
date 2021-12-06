#https://codeforces.com/problemset/problem/231/A
n = int(input())
solved = 0
for i in range(n):
    problem = input()
    if (problem.count("1") >= 2):
        solved += 1
print(solved)