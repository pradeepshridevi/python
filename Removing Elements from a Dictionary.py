my_dict = {
    "name": "Pradeep",
    "age": 18,
    "city": "Tumkur",
    "country": "INDIA"
}

def delete_element(key):
    if key in my_dict:
        del my_dict[key]  
        print(f"Deleted: {key}")
    else:
        print(f"Key '{key}' not found in the dictionary.")
delete_element("age")
delete_element("gender")
print("\nFinal Dictionary:")
print(my_dict)
