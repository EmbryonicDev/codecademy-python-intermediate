song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electric']}

user_tag_1 = 'warm'
user_tag_2 = 'exciting'
user_tag_3 = 'electric'

# Write your code below!
# Checkpoint 1
print('Original song data:', song_data)
tag_set = set(song_data['Retro Words'])
# Checkpoint 2
tag_set.update([user_tag_1, user_tag_2, user_tag_3])
# Checkpoint 3
song_data['Retro Words'] = list(tag_set)
print('New song data:', song_data)
