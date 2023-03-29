song_data = {
    'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
    'Wait For Limit': ['rap', 'upbeat', 'romance'],
    'Stomping Cue': ['country', 'fiddle', 'party'],
    'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
    'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
    'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
    'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
    'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']
}

user_recent_songs = {
    'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
    'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat']
}

# Step 1: Find intersection of tags for recent songs
tags_int = set(user_recent_songs['Retro Words']).intersection(
    set(user_recent_songs['Lowkey Space']))
print(tags_int)

# Step 2: Find recommended songs based on common tags
recommended_songs = {}
for song, tags in song_data.items():
    if song not in user_recent_songs and set(tags).intersection(tags_int):
        recommended_songs[song] = tags

print(recommended_songs)
