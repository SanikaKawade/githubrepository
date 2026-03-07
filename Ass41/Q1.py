import math

data = [
("A",1,2,"Red"),
("B",2,3,"Red"),
("C",3,1,"Blue"),
("D",6,5,"Blue")
]

x = int(input("Enter X coordinate: "))
y = int(input("Enter Y coordinate: "))

distances = []

for point in data:
    name,px,py,label = point

    d = math.sqrt((x-px)**2 + (y-py)**2)

    distances.append((name,d,label))

distances.sort(key=lambda x: x[1])

k = 3

neighbors = distances[:k]

print("Nearest Neighbors:")

red = 0
blue = 0

for n in neighbors:
    print(n[0],"- Distance:",round(n[1],2))

    if n[2]=="Red":
        red +=1
    else:
        blue +=1

if red>blue:
    print("Predicted Class: Red")
else:
    print("Predicted Class: Blue")
for k in [1,3,5]:

    neighbors = distances[:k]

    red = 0
    blue = 0

    for n in neighbors:
        if n[2]=="Red":
            red +=1
        else:
            blue +=1

    if red>blue:
        result="Red"
    else:
        result="Blue"

    print("K =",k,"->",result)
import math

data = [
(2,60,"Fail"),
(5,80,"Pass"),
(6,85,"Pass"),
(1,50,"Fail")
]

study = int(input("Enter Study Hours: "))
att = int(input("Enter Attendance: "))

distances = []

for d in data:
    sh,at,label = d

    dist = math.sqrt((study-sh)**2 + (att-at)**2)

    distances.append((dist,label))

distances.sort()

k = 3

neighbors = distances[:k]

pass_count = 0
fail_count = 0

for n in neighbors:
    if n[1]=="Pass":
        pass_count+=1
    else:
        fail_count+=1

if pass_count>fail_count:
    print("Predicted Result: Pass")
else:
    print("Predicted Result: Fail")