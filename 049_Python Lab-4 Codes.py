#Post Labs
#1
list = [2, 3, 4, 5]
result = 1
for num in list:
    result *= num
print("Product of all items:", result)

#2
list = [5, 12, 7, 20, 3]
largest = max(list)
print("Largest number:", largest)

#3
my_list = [1, 2, 2, 3, 4, 4, 5]
removed_list = list(dict.fromkeys(my_list))
print("List without duplicates:", removed_list)

#4
my_list = ['a', 'b', 'a', 'c', 'b', 'a']
frequency = {}
for item in my_list:
    frequency[item] = frequency.get(item, 0) + 1
print("Frequency of elements:", frequency)

#5
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = list(set(list1) & set(list2))
print("Common items:", common)

#6
int_list = [1, 2, 3, 4]
combined = int("".join(map(str, int_list)))
print("Combined integer:", combined)
