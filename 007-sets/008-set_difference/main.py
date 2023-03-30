import itertools

song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_liked_song = {'Back To Art': ['pop', 'sad', 'emotional', 'relationship']}
user_disliked_song = {'Retro Words': [
    'pop', 'warm', 'happy', 'electronic', 'synth']}

# Write your code below!
print('\nCheckpoint 1')
tag_diff = set(user_liked_song['Back To Art']).difference(
    user_disliked_song['Retro Words'])

for tag in tag_diff:
    print(tag)

print('\nCheckpoint 2')
recommended_songs = {}
for song, tags in song_data.items():
    if (song not in itertools.chain(user_disliked_song, user_liked_song)
            and set(tags).intersection(tag_diff)):
        recommended_songs[song] = tags

print(recommended_songs)
