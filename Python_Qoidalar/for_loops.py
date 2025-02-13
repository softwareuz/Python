i = int(input("Eneter starting position:"))
x = int(input("Enter ending position:"))
s = int(input("Enter step:"))
for i in range(i , x , s):
    print(i)
for i in reversed(range(i,x,s)):
    print(i)
for x in range(1, 10):
    if x == 2:
        continue  # skip entered number
    else:
        print(x)


for x in range(1 , 20):
    if x == 7:
        break
    else:
        print(x)

