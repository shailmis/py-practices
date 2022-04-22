# Example of sorted function
color_list = ["green","red","Red","GREEN","white","black"]
numbers = (101,11,12,322,4,34)
another_number_list = (11,12,4,34,565,76,78)
color_list_sorted = sorted(color_list)
print(f"Sorted list {color_list_sorted}")
sorted_numbers = sorted(numbers, reverse=True)
print(f"Sorted numbers {sorted_numbers}")
print(type(sorted_numbers))
print(type(numbers))
another_number_list_reversed = list(reversed(another_number_list))
print(another_number_list_reversed)
