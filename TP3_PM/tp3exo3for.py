import time
n = int(input("temp compte a rebour :"))
for i in range(0,n):
    print(n,flush=True)
    n = n - 1
    time.sleep(1)

print("fin !")