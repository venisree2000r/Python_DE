list1 = [1, 2, 3, 4]
# Method 1
print(list1[::-1])
# Method 2
list1.reverse()
print(list1)

list2 = [1, "hello", 3.14, True, [5, 6]]
# Method 1: slicing
print(list2[::-1])
# Method 2: reverse() method
list2.reverse()
print(list2)

# Q2: Remove duplicates from list
list3 = [1, 2, 2, 3, 4, 4]
unique = list(set(list3))
print(unique)

# Q3: Find second largest number
list4 = [10, 20, 4, 45, 99]
list4 = list(set(list4))
list4.sort()
print(list4[-2])

# Q4: Convert tuple to list
tuple1 = (1,2,"veni")
my_list = list(tuple1)
print(my_list)

# Q5: Count occurrences in tuple
t = (1, 2, 2, 3, 2, 2)
print(t.count(2))

# Q6: Merge two dictionaries
d1 = {'a': 1}
d2 = {'b': 2}
d1.update(d2)
print(d1)

# Q7: Sort dictionary by value
d = {'a': 3, 'b': 1, 'c': 2}
sorted_dict = dict(sorted(d.items(), key=lambda x: x[1]))
print(sorted_dict)

# Q8: Check key exists
d = {'a': 1, 'b': 2}
if 'a' in d:
    print("Exists")

# SETS
# Q9: Find intersection
a = {1, 2, 3, 4}
b = {2, 3, 4}
print(a & b)

# Q10: Remove duplicates using set
lst = [1, 2, 2, 3]
print(list(set(lst)))

# String Questions
# Q11: Check palindrome
s = "madam"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

# Q12: Count vowels
word = "hello"
vowels = "aeiou"
count = sum(1 for char in word if char in vowels)
print(count)

# Q13: Fibonacci series
n = 10
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

