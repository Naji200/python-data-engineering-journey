#liste
my_list = [1, 2, 3, 2]

print(my_list[0])      # 1
my_list.append(4)      # adds 4
my_list.remove(2)      # removes first 2
print(my_list)         # [1, 3, 2, 4]

#tuple
my_tuple = (1, 2, 3, 2)
print(my_tuple[0])     # 1

#set
my_set = {1, 2, 3, 2}
print(my_set)          # {1, 2, 3}

my_set.add(4)
my_set.remove(2)
print(my_set)

#dictionary
my_dict = {
    "name": "Naji",
    "age": 24,
    "city": "Casablanca"
}

print(my_dict["name"])     # Naji
my_dict["age"] = 25
my_dict["job"] = "Data Engineer"

print(my_dict)


def reverse_list(lst):
    return lst[::-1]
print(reverse_list([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]

def max_in_list(lst):
    return max(lst)
print(max_in_list([1, 2, 3, 4, 5]))  # 5

def count_occurrences(lst, value):
    return lst.count(value)
print(count_occurrences([1, 2, 3, 2, 4], 2))  # 2

def count_occurrences2(lst):
    for i in set(lst):
        print(f"{i}: {lst.count(i)}")
count_occurrences2([1, 2, 3, 2, 4])

