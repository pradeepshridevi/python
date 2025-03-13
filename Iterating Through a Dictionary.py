my_dict = {
    "name": "pradeep",
    "age": 18,
    "city": "Tumkur",
    "country": "INDIA"
}
def print_keys_values(dictionary):
    for key, value in dictionary.items():
        print(f"Key: {key}, Value: {value}")
print_keys_values(my_dict)
