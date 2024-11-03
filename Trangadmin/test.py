import  math
def fibonaci(n):
    if(n<=1):
        return n
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a+b
    return b

def UCLN(a,b):
    if(b==0):
        return a
    return UCLN(b,a%b)

A = int(input("Nhập số nguyên dương A: "))
B = int(input("Nhap so nguyen duong B: "))
M = int(input("Nhập số nguyên dương M: "))

U = math.gcd(fibonaci(A), fibonaci(B))
ketQua = U % M
print(ketQua)