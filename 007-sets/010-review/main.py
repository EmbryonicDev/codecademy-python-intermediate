from print_checkpoint import print_checkpoint

music_tags = {'pop', 'warm', 'happy', 'electronic', 'synth', 'dance', 'upbeat'}

# Write your code below!
print_checkpoint(1)
my_tags = frozenset({'pop', 'electronic', 'relaxing', 'slow', 'synth'})
print('my_tags printed:\n', my_tags)

print_checkpoint(2)
frozen_tag_union = my_tags.union(music_tags)
print('frozen_tag_union printed:\n', frozen_tag_union)

print_checkpoint(3)
regular_tag_intersect = music_tags.intersection(my_tags)
print('regular_tag_intersect printed:\n', regular_tag_intersect)

print_checkpoint(4)
frozen_tag_difference = my_tags.difference(music_tags)
print('frozen_tag_difference printed:\n', frozen_tag_difference)

print_checkpoint(5)
regular_tag_sd = music_tags.symmetric_difference(my_tags)
print('regular_tag_sd printed:\n', regular_tag_sd)
