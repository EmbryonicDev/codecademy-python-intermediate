guests = {}


def read_guestlist(file_name):
    text_file = open(file_name, 'r')
    while True:
        line_data = text_file.readline().strip().split(",")
        if len(line_data) < 2:
            # If no more lines, close file
            text_file.close()
            break
        name = line_data[0]
        yield name
        age = int(line_data[1])
        guests[name] = age

# Checkpoint 1   
guest_list = read_guestlist('guest_list.txt')
for i in range(10):
        print(f"{i+1}: {next(guest_list)}")