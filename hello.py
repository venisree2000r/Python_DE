set1 = set('abcdefgk')
set2 = set('abcdgi')

print(set1 - set2) # remove same values
print(set1 | set2) # print all values + remove duplicates
print(set1 & set2) # print only common values
print(set1 ^ set2) # print not common values


keys = ["Ravichandran", "Saraswathy", "NaveenKumar", "Venisree"]
values = [52, 50, 29, 26]
family_info = dict(zip(keys, values))
print(family_info)

a = "venisree"
b = "venisree"
print(id(a) == id(b))



# Functions

