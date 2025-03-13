dict1 = {
    "name": "Pradeep",
    "age": 18
}

dict2 = {
    "city": "Tumkur",
    "country": "INDIA"
}
def merge_dicts(dict1, dict2):
    merged_dict = dict1.copy() 
    merged_dict.update(dict2)   
    return merged_dict
merged_dict = merge_dicts(dict1, dict2)
print("Merged Dictionary:")
print(merged_dict)
