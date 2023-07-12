# Asking for the number of rows and columns
rows = int(input("Enter the no. of rows you want: "))
columns = int(input("Enter the no. of columns you want: "))

# Creating the 2D empty List
List = []

# iterate through each row and column and prompt the user for input 
for i in range(rows):
    row = []
    for j in range(columns):
        row.append(input("Enter a value for row" + str(i+1) +str(j+1) + ":" ))
    List.append(row)

# Displaying the output

# printing the 2D list
print("The 2D List is : ",List)

# print the each row of the 2D list 
print("The rows of the 2D list are :")
for row in List:
    print(row)

