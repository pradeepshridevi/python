def merge_and_remove_duplicates_ordered(list1, list2):
    merged_list = list1 + list2
    unique_list = []
    for item in merged_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list
