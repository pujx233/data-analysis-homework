def maxSideLength(t,mat=[]):
    m,n = len(mat),len(mat[0])
    P = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            P[i][j] = P[i-1][j] + P[i][j-1]-P[i-1][j-1] +mat[i-1][j-1]
    def getR(x1,y1,x2,y2):
        return P[x2][y2] - P[x1 - 1][y2] - P[x2][y1 - 1] + P[x1 - 1][y1 - 1]

    l, r, ans = 1, min(m, n), 0
    while l <= r:
        mid = (l + r) // 2
        find = any(getR(i, j, i + mid - 1, j + mid - 1) <= t for i in range(1, m - mid + 2) for j in
                   range(1, n - mid + 2))
        if find:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans
if __name__=='__main__':
    list = []
    for _ in range(int(input())):
        lis = [int(i) for i in input().split(',')]
        list.append(lis)
    n = int(input())
    print(maxSideLength(n,list))