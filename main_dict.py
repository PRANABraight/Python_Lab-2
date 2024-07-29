# Example usage of dictionary_operations.py

# Import the module
import module_dict as do

# Define some dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 5}
dict3 = {'a': 1, 'b': 2, 'e': 6}

print("--------------------------------------------------------")

merged = do.merging_Dict(dict1, dict2, dict3)
print("Merged Dictionary:", merged)
print("--------------------------------------------------------")

common_keys_result = do.common_keys(dict1, dict2, dict3)
print("Common Keys:", common_keys_result)
print("--------------------------------------------------------")

inverted_dict = do.invert_dict(dict1)
print("Inverted Dictionary:", inverted_dict)
print("--------------------------------------------------------")

common_pairs = do.common_key_value_pairs(dict1, dict2, dict3)
print("Common Key-Value Pairs:", common_pairs)
print("--------------------------------------------------------")
