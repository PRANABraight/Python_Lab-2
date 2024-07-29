#  2. Write a Python program to create a module that performs various set operations.
# a. Write a function to add an element to a set, ensuring no errors if the element is already  present.
# b. Write a function to remove an element from a set, ensuring no errors if the element is  not present.
# c. Write a function to return the union and intersection of two sets, handling empty sets  correctly.
# d. Write a function to return the difference S1−S2, handling empty sets correctly.
# e. Write a function to check if set S1 is a subset of set S2, handling empty sets correctly.
# f. Write a function to find the length of a set without using the len() function.
# g. Write a function to compute the symmetric difference of two sets.
# h. Write a function to compute the power set of a given set.
# i. Write a function to get all unique subsets of a given set.
# Implement this module and demonstrate it by using adequate examples.



def add(set1,value):
  set1.add(value)
  return set1

def remove(set1,value):
  set1.remove(value)
  return set1

def union(set1,set2):
  return set1.union(set2)

def intersection(set1,set2):
  return set1.intersection(set2)

def difference(set1,set2):
  return set1.difference(set2)

def issubset(set1,set2):
  return set1.issubset(set2)

def length(set1):
  count = 0
  for i in set1:
    count += 1
  return count

def symmetric_difference(set1,set2):
  return set1.symmetric_difference(set2)

def power_set(set1):
  power_set = [[]]
  for i in set1:
    for j in power_set:
      power_set = power_set + [j + [i]]
  return power_set

def unique_subsets(set1):
  unique_subsets = [[]]
  for i in set1:
    for j in unique_subsets:
      unique_subsets = unique_subsets + [j + [i]]
  unique_subsets.remove([])
  return unique_subsets
