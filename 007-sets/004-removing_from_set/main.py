song_data_users = {'Retro Words': [
    'pop', 'onion', 'warm', 'helloworld', 'happy', 'spam', 'electric']}

# Write your code below!
# Checkpoint 1
tag_set = set(song_data_users['Retro Words'])
# Checkpoint 2
for tag in ['onion', 'helloworld', 'spam']:
    tag_set.remove(tag)
# Checkpoint 3
song_data_users['Retro Words'] = tag_set
print(song_data_users)
