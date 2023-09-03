#--1--# Array Initialization:
my_list = []

for i in range(1, 11):
    my_list.append(i)
    print(my_list)
    
    
#--2--# Array Slicing:
my_arr = [12, 13, 14, 15, 16, 17, 18, 19, 20]
print("My sub array: ", my_arr[2:6])


#--3--# Array Sum:
my_arr = [12, 13, 14, 15, 16, 17, 18, 19, 20]
def calculate_sum(arr):
    sum = 0
    for i  in arr:
        sum += i
    return sum
print(calculate_sum(my_arr))


#--4--# Array Maximum:
my_arr = [12, 13, 14, 15, 16, 17, 18, 19, 20]

max_value = my_arr[0]
my_index = 0

for i in range(1, len(my_arr)):
    if my_arr[i] > max_value:
        max_value = my_arr[i]
        my_index = i
        
print("Maximum Value:", max_value, ", Index:", my_index)


#--5--# Array Reversal:
my_arr = [12, 13, 14, 15, 16, 17, 18, 19, 20]
my_arr.reverse()
print(my_arr)


#--6--# Array Sorting:
my_arr = [12, 3, 14, 5, 1, 7, 18, 19, 2]
my_arr.sort()
print("Sorted Array:", my_arr)


#--7--# Array Search:
# sourcery skip: return-or-yield-outside-function

def search_number(arr, my_num):
    for i in range(len(arr)):
        if arr[i] == my_num:
            return i
    return -1

my_arr = [12, 3, 14, 5, 1, 7, 18, 19, 2]
my_num = int(input("Enter your number: "))

result = search_number(my_arr, my_num)

if result != -1:
    print("Number found", my_num , " at index:", result)
else:
    print("Number not found in an array :", result)


#--8--# Array Concatenation:
my_arr1 = [12, 3, 14,]
my_arr2 = [5, 1, 7,]

concatenated_array = my_arr1 + my_arr2
print("My Concatenated Array: ", concatenated_array)


#--9--# Array Removal:
my_arr = [12, 3, 14, 5, 1, 3, 7, 18, 3, 19, 2]
target = 3
modified_array = []

for i in my_arr:
    if i != target:
        modified_array.append(i)
print(modified_array)


#--10--# Array Unique Elements:
my_arr = [12, 3, 14, 5, 1, 3, 7, 2, 18, 3, 19, 2, 5, 1, 3, 7,]
my_arr.sort()
new_arr = set(my_arr)
modified_arr = list(new_arr)
print(modified_arr)