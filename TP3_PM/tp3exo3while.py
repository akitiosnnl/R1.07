import time

from win32trace import flush

n = int(input("temp compte a rebour :"))

while n != 0:
    time.sleep(1)
    print(n,flush=True)
    n = n-1

print("fin !")