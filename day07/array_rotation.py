# List Rotation

test_list = [5, 6, 7, 8, 1, 11, 15, 16]

print("Original list:", str(test_list))

new_list = test_list[4:] + test_list[:4]

print("List after rotation:", str(new_list))