# arr = [4,5,7,9,2]
how_many = int(input('how many numbers do you want to add:'))
arr = []

for i in range(how_many):
    arr.append(int(input('enter the number:')))
#second phase
max = arr[0]
min = arr[0]
for i in range(len(arr)):
    element = arr[i]
    if element > max:
        max = element
    if element < min:
        min = element

print('The max element is: ',max)
print('The min element is: ',min)