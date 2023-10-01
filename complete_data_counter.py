import csv
f = open("record.csv", "r")
reader = csv.reader(f)
outList = list()
for i in reader:
    outList.append(i)

# count = 0
# for data in outList:
    
#     i = 96
#     while (i <= 101):
#         if (data[i] != "TRUE"):
#             i += 1
#             break
#         i += 1
#     else:
#         count += 1

count = 0
i = 0
while (i < len(outList)):

    if (outList[i][96 : 102] == ["TRUE" for j in range(6)] and "null" not in outList[i][8 : 92]):
        count += 1

    i += 1

print(count)
input()
