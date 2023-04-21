N = int(input('Введіть число: '))

if N %2 and N <= 20:
    print("Weird")
    exit()
if not N %2 and 2 <= N <= 5:
    print("Not Weird")
    exit()
if not N %2 and 6 <= N <= 20:
    print("Weird")
    exit()
if N %2 and N >= 20:
    print("Not Weird")
    exit()
