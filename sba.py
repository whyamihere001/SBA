guest = []
for i in range(0,3):
    guest = guest + [[]]
    for j in range(0,4):
        guest[i] = guest[i] + ['']
    
for i in range(0,3):
    guest[i][0] = input("input your name")
    guest[i][1] = input("input your gender M/F")
    
    
#initializing table1 for F, table2 for M
for i in range(0,3):
    if guest[i][1] == "F":
        guest[i][2] = "1"
    else:
        guest [i][2] == "2"
        
print()
print()
print("***********************")
print("Table Allocation")
print("***********************")
print("Table 1:")
for i in range(0,3):
    if guest[i][2] == "1":
        print("guest[i][0]")
print()
print("Table 2")
for i in range(0,3):
    if guest[i][2] == "2":
        print(guest[i][0])

#menu
while True:
    print("1:Registration")
    print("2:Generate seating plan")