def get_word_count(book_text):
    words = book_text.split()
    return len(words)


def get_character_count(book_text):
    character_count = {}
    lower_text = book_text.lower()
    for char in lower_text:
        if char not in character_count:
            character_count[char] = 1
        else:
            character_count[char] += 1
    return character_count

def sort_stats(count):
    report = []
    for i in count:
        report.append({"char": i, "num": count[i]})
    def sorter(report):
        return report["num"]
    report.sort(reverse = True, key = sorter)
   
   
    return report
