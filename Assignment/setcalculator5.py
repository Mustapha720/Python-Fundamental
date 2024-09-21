# 1. Create a set calculator
# print('ONLY INPUT THREE NUMBERS')
set1 = set(input('Input your first set: '))
set2 = set(input('Input your second set: '))
set3=set1.union(set2)
set4=set1.intersection(set2)
set5=set1.difference(set2)
set6=set1.issubset(set2)
set7=set1.issuperset(set2)
set8=set1.isdisjoint(set2)

print("\n1. Union")
print("2. Intersection")
print("3. Difference")
print("4. Issubset")
print("5. Issuperset")
print("6. Isdisjoint")
choice = input('Pick an operation: ')
if choice == '1':
    print(set3)
elif choice == '2':
    print(set4)
elif choice == '3':
    print(set5)
elif choice == '4':
    print(set6)
elif choice == '5':
    print(set7)
elif choice == '6':
    print(set8)
else:
    print("Error")



"""
LECTURER'S SOLUTION
list_of_sets = []
num_of_set=int(input('HOW MANY SET DO YOU WANT TO WORK WITH? '))
for each_set in range(1, num_of_set+1):
    set_items=[]
    items=int(input(f'HOW MANY VALUES ARE IN SET {each_set}? '))
    for itm in range(1, items+1):
        item=input(f'ENTER VALUE {itm}: ')
        set_items.append(item)
    list_of_sets.append(set(set_items))
print(list_of_sets)
"""