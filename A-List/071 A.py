#https://codeforces.com/problemset/problem/71/A
cases = int(input())
while cases>0:
    wrd = input()
    if(len(wrd)>10):
        first = wrd[0]
        lst = wrd[-1]
        l = len(wrd) - 2
        enc = str(first) + str(l) + str(lst)
        print(enc)
    else:
        print(wrd)
    cases-=1