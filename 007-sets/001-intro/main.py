genre_results = ['rap', 'classical', 'rock', 'rock', 'country', 'rap', 'rock', 'latin', 'country', 'k-pop', 'pop', 'rap', 'rock', 'k-pop',
                 'rap', 'k-pop', 'rock', 'rap', 'latin', 'pop', 'pop', 'classical', 'pop', 'country', 'rock', 'classical', 'country', 'pop', 'rap', 'latin']

# Write your code below!
print(f"\nCheckpoint 1")
survey_genres = set(genre_results)
for genre in survey_genres:
    print(genre)

print(f"\nCheckpoint 2")
survey_abbreviated = set(x[0:3] for x in genre_results)
for genre in survey_abbreviated:
    print(genre)
