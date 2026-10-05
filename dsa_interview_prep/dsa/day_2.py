def first_non_repeating(word: str)-> int:
    """Counts the first non repeating letters."""

    count = {}

    for letter in word:
        count[letter] = count.get(letter, 0) + 1

    for i, letter in enumerate(word):
        if count[letter] == 1:
            return letter

    return None

print(first_non_repeating("leetcode"))
print(first_non_repeating("aabb"))