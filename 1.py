def square(list_nums):
    for i in range(len(list_nums)):
        list_nums[i] = list_nums[i]**2
    print(list_nums)

string = input("Enter the elements of the list separated by space: ")
list = string.split()
list_nums = [int(i) for i in list] 

square(list_nums)
