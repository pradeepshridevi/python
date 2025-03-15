def access_list_element(lst, index):
    try:
      
        element = lst[index]
        print(f"Element at index {index}: {element}")
    except IndexError:
        
        print(f"Error: Index {index} is out of range. The list has only {len(lst)} elements.")
    except Exception as e:
        
        print(f"An unexpected error occurred: {e}")


def main():
    
    my_list = [10, 20, 30, 40, 50]

  
    indices_to_access = [2, 5, -1, 10]

    for index in indices_to_access:
        access_list_element(my_list, index)

if __name__ == "__main__":
    main()
