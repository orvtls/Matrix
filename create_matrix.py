rows = int(input("enter the number of rows:"))
columns = int(input("enter the number of columns:"))
output = []
for i in range(rows):
    l1 = []
    for j in range(columns):
        l1.append(int(input()))
    output.append(l1)
print("The matrix is:")
print(output)

