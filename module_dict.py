# # 3. Write a program to create functions that can accept multiple dictionaries as arguments using
# # ‘*args’, and perform various operations on them.
# # (a) Write a function, say, ‘merging_Dict(*args)’ that takes multiple dictionaries and merge
# # them.
# (b) Write a function which can find common keys in multiple dictionaries.

# (c) Create a function to invert a dictionary, swapping keys and values. If multiple keys have
# the same value, group these keys in a list in the inverted dictionary. Implement and demonstrate
# this with examples.
# (d)Write a function to find common key-value pairs across multiple dictionaries.


def merging_Dict(*args):
  merged_dict = {}
  for i in args:
    merged_dict.update(i)
  return merged_dict

def common_keys(*args):
  common_keys = set(args[0].keys()).intersection(*args[1:])
  return common_keys


def invert_dict(d):
  inverted_dict = {}
  for key, value in d.items():
    if value in inverted_dict:
      inverted_dict[value].append(key)
    else:
      inverted_dict[value] = [key]
  return inverted_dict

def common_key_value_pairs(*args):
  common_key_value_pairs = set(args[0].items()).intersection(*args[1:])
  return common_key_value_pairs
