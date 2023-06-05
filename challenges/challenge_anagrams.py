# https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OMergeSort.html
# utilizei como base esse link

def ordenando(word):
    if len(word) <= 1:
        return word

    meio = len(word) // 2
    left = word[:meio]
    right = word[meio:]

    left = ordenando(left)
    right = ordenando(right)

    word_merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            word_merged.append(left[i])
            i += 1
        else:
            word_merged.append(right[j])
            j += 1

    while i < len(left):
        word_merged.append(left[i])
        i += 1

    while j < len(right):
        word_merged.append(right[j])
        j += 1

    return word_merged


def is_anagram(first_string, second_string):
    if not len(first_string) or not len(second_string):
        return False

    first_string = first_string.lower()
    second_string = second_string.lower()

    first_string_sort = ordenando(list(first_string))
    second_string_sort = ordenando(list(second_string))

    return (''.join(first_string_sort),
            ''.join(second_string_sort),
            first_string_sort == second_string_sort)
