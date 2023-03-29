song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth']}

user_tag_data = {'Lowkey Space': ['party', 'synth', 'fast', 'upbeat'],
                 'Retro Words': ['happy', 'electronic', 'fun', 'exciting'],
                 'Wait For Limit': ['romance', 'chill', 'rap', 'rhythmic'],
                 'Stomping Cue': ['country', 'swing', 'party', 'instrumental']}

# Write your code below!
# Checkpoint 1
new_song_data = {}
# Checkpoint 2
# Loop over song_data and create a new set for each category
for title, tags in song_data.items():
    new_song_data[title] = set(tags) | set(user_tag_data[title])

# Print the new dictionary
print(new_song_data)
