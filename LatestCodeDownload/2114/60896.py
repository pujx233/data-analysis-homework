def find(n):
    while (n % 4 == 0): n /= 4
    if ( n % 8 == 7): return(4)
    a = 0
    while ( (a * a) <= n):
        b = int(pow((n - a * a),0.5))
        if(a * a + b * b == n) :
            if(a != 0 and b != 0):
                return(2)
            else:
                return(1)
        a+=1
    return(3)

a=eval(input())
print(find(a))