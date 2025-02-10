def fibo (figure) :
    if figure <= 1:
        return figure
    else :
        return fibo(figure - 1) + fibo(figure - 2)

for i in range(10) :
    print(fibo(i))