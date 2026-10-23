def fun(n):
    x = 2
    count = 0
    while count < n:
        for d in range(2, int(x**0.5) + 1):
            if x % d == 0:
                break
        else:                 # runs only if the for loop did NOT break
            print(x)
            count += 1
        x += 1                # outside the for loop

n = 10
fun(n)
