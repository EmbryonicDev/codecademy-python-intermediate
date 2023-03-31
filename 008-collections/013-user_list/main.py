from collections import UserList

data = [4, 6, 8, 9, 5, 7, 3, 1, 0]

# Write your code below!


class ListSorter(UserList):

    def append(self, value_to_add):
        self.data.append(value_to_add)
        self.data.sort()


sorted_list = ListSorter(data)
print('\nsorted_list before appending "2":\n', sorted_list)

sorted_list.append(2)
print('\nsorted_list after appending "2":\n', sorted_list)
