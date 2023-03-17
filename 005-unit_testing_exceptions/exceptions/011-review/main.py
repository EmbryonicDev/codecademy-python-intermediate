instrument_familes = {
    'Strings': ['Guitar', 'Banjo', 'Sitar'],
    'Percussion': ['Conga', 'Cymbal', 'Cajon'],
    'woodwinds': ['Flute', 'Oboe', 'Clarinet']
}


def print_instrument_families():
    for family in ['Strings', 'Percussn', 'woodwinds']:
        try:
            print(
                f"Some instruments in the {family} family are: {instrument_familes[family]}")
        except KeyError as e:
            print(f"Instrument family: {e} is not in my database.")


print_instrument_families()
