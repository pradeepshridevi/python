my_dict = {}
my_dict = {}
def add_element(key, value):
    my_dict[key] = value
    print(f"Added: {key} -> {value}")
def update_element(key, value):
    if key in my_dict:
        my_dict[key] = value
        print(f"Updated: {key} -> {value}")
    else:
        print(f"Key '{key}' not found in the dictionary.")
add_element("name", "pradeep")
add_element("age", 17)
add_element("city", "tumkur")
update_element("age", 18)
update_element("country", "INDIA")
print("\nFinal Dictionary:")
print(my_dict)
