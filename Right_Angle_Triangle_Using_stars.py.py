# for rows in range(4):
#     for column in range (rows):
#         print(column, end=" ")
# print(rows)


def rightAngTri():
    x = int(input("Enter X: "))
    for i in range (x):
        for j in range (i):
          print("*", end=" ")
        print("*")

rightAngTri()


