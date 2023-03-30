user_song_history = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Stomping Cue': ['country', 'fiddle', 'party'],
                     'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
                     'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

friend_song_history = {'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
                       'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
                       'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
                       'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

# Write your code below!
print('\nCheckpoint 1')
user_tags = set()
for song, tags in user_song_history.items():
    user_tags.update(tags)
print('user_tags printed:\n', user_tags)

print('\nCheckpoint 2')
friend_tags = set()
for song, tags in friend_song_history.items():
    friend_tags.update(tags)
print('friend_tags printed:\n', friend_tags)

print('\nCheckpoint 3')
unique_tags = user_tags.symmetric_difference(friend_tags)
print('unique_tags printed:\n', unique_tags)
