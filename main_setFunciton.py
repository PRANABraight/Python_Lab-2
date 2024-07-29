from module_SetFunction import *

set1 = {1,2,3,4,5}
set2 = {4,5,6,7}


print("--------------------------------------------------------")

print("Added a element 6: ", add(set1, 6))
print("--------------------------------------------------------")

print("Removed a element 3: ", remove(set1, 3))
print("--------------------------------------------------------")

print("Union of two sets  {1,2,3,4,5} and  {4,5,6,7}: ", union(set1,set2))
print("--------------------------------------------------------")

print("Intersection of two sets  {1,2,3,4,5} and  {4,5,6,7}: ", intersection(set1,set2))
print("--------------------------------------------------------")

print("Difference of two sets  {1,2,3,4,5} and  {4,5,6,7}: ", difference(set1,set2))
print("--------------------------------------------------------")

print("Checking if {1,2,3,4,5} is subset  {4,5,6,7}: ", issubset(set1,set2))
print("--------------------------------------------------------")

print("Length of {4,5,6,7}: ", length(set2))
print("--------------------------------------------------------")

print("Symmetric difference of {1,2,3,4,5} and {4,5,6,7}: ", symmetric_difference(set1,set2))
print("--------------------------------------------------------")

print(f"Power set of {set1}: \n", power_set(set1))
print("--------------------------------------------------------")

print("All the unique subset of {1,2,3,4,5}: \n", unique_subsets(set1))
print("--------------------------------------------------------")




