allowed_tags = ['pop', 'hip-hop', 'rap', 'dance', 'electronic', 'latin', 'indie', 'alternative rock', 'classical', 'k-pop', 'country', 'rock', 'metal', 'jazz',
                'exciting', 'sad', 'happy', 'upbeat', 'party', 'synth', 'rhythmic', 'emotional', 'relationship', 'warm', 'guitar', 'fiddle', 'romance', 'chill', 'swing']

song_data_users = {'Retro Words': ['pop', 'explosion', 'hammer', 'bomb',
                                   'warm', 'due', 'writer', 'happy', 'horrible', 'electric', 'mushroom', 'shed']}

# Write your code below!
print(f"\nCheckpoint 1")
tag_set = set(song_data_users['Retro Words'])
print(tag_set)

print(f"\nCheckpoint 2")
bad_tags = []
for tag in tag_set:
    if tag not in allowed_tags:
        bad_tags.append(tag)
print(bad_tags)

print(f"\nCheckpoint 3")
print('user tags before removing bad tags:\n', tag_set)
for tag in bad_tags:
    tag_set.discard(tag)

print(f"\nCheckpoint 4")
song_data_users['Retro Words'] = tag_set
print('user tags after removing bad tags:\n', tag_set)
