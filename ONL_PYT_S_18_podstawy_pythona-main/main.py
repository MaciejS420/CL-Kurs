def create_list(x, y):
    return [x, y] * 4


print(create_list(1, 2))

countries = {
    'poland': 'warsaw',
    'germany': 'berlin',
    'italy': 'rome'
}


def list_keys(d):
    result = []

    for key in d:
        result.append(key)

    return result














def find_short_words(words):
    short_words = []
    for word in words:
        if len(word) < 5:
            short_words.append(word)


















def sum_(numbers):
    result = numbers[0]

    for number in numbers[1:]:
        result += number
        return result


print(sum_([1, 2, 3, 4]))