m = int(input("Enter the number of rows:"))
n = int(input("Enter the number of columns:"))
output1 = []
for i in range(m):
    l1 = []
    for j in range(n):
        l1.append(int(input()))
    output1.append(l1)
print("The first matrix is:")
print(output1)

print("Now enter the values for the second matrix:")
output2 = []
for q in range(m):
    l2 = []
    for t in range(n):
        l2.append(int(input()))
    output2.append(l2)
print("The second matrix is:")
print(output2)
sum_matrix = []
for c in range(len(output1)):
    l3 = []
    for y in range(len(output1[0])):
        s = output1[c][y] + output2[c][y]
        l3.append(s)
    sum_matrix.append(l3)
print("The sum is:")
print(sum_matrix)


