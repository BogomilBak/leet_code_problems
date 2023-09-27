import re


def remove_numerations_timestamps(text):
    # Remove numerations
    text = re.sub(r'\b\d+\b', '', text)

    # Remove timestamps with symbols
    text = re.sub(r'\d{2}:\d{2}:\d{2},\d{3} ::, --> ::, \d{2}:\d{2}:\d{2},\d{3}', '', text)

    # Remove empty lines
    text = re.sub(r'\n\s*\n', '\n', text)

    return text.strip()


# Example usage
text = '''12
00:02:00,555 ::, --> ::, 00:02:02,296
Добре, готови ли сте, момчета?

13
00:02:02,470 ::, --> ::, 00:02:04,820
Ракестрау, ти и аз,
поемаме фронта.

...'''

result = remove_numerations_timestamps(text)
end_result = result.replace("::, ::, --> ::, ::,", '')
print(end_result)
