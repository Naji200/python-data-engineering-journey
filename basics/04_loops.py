nu = 100
for i in range(nu):
    print(i)
N = 0
for i in range(nu):
    N = N +(i)
    print(N)

n = 0
for i in range(nu):
    n = n + i
print(n)  
          


tbale = int(input("enter a number: "))
for i in range(1, 11):
    print(f"{tbale} x {i} = {tbale * i}")

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")


for i in range(1, 51):
    if i%2 == 0:
        print(i)


while i < 50:
    if i%2 == 0:
        print(i)
    i = i + 1
    