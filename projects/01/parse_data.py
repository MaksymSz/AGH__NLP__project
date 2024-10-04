import re
from collections import Counter


def read_file(filename: str) -> str:
    with open(filename, "r", encoding='utf-8') as f:
        content = f.readlines()[11:20000]
    return ''.join(content)


def clear_tags(text: str) -> str:
    without_closing_tags = ''.join(text.split('</text>'))
    clear_txt = re.sub(r'<text .*>', '', without_closing_tags)
    return clear_txt


def clear_text_from_punctuation(text: str) -> str:
    return re.sub(r'[.,|/\-?!"\'()\[\]]', '', text)


def count_freq_of_words_in_text(text: str) -> dict[str, int]:
    cleared_txt = clear_text_from_punctuation(text)
    items = cleared_txt.split()
    freq_of_words = dict(Counter(items))
    return dict(sorted(freq_of_words.items(), key=lambda x: x[1], reverse=True))


# zwraca dict ze słowem i listą słów które po nim występują (tak może uniknie się powtórzeń połączeń w grafie)
def get_neighbours(text: str) -> dict[str, list[str]]:
    items = text.split()
    neighbours = {}
    for i in range(len(items) - 1):
        word = items[i]
        if word in neighbours :
            neighbours[word].append(items[i + 1])
        else:
            neighbours[word] = [items[i + 1]]
    unique_neighbors = {k: list(set(v)) for k, v in neighbours.items()}
    return dict(sorted(unique_neighbors.items(), key=lambda x: len(x[1])))


# zwraca dict z kluczem będącym liczbą procentem i listą slow ktore zawieraja sie w tym procencie
def percentage_of_language(freq: dict[str, int]) -> dict[int, list[str]]:
    number_of_words = sum(freq.values())
    percentage_of_words = {k: v / number_of_words for k, v in freq.items()}
    final_percentage = {i * 10: [] for i in range(1, 11)}
    val = 0
    for k, v in percentage_of_words.items():
        for i, j in final_percentage.items():
            if i / 100 > val:
                final_percentage[i].append(k)
        val += v
    return final_percentage


def main() -> None:
    text = read_file("../../data/corpus_raw.txt")
    italian_text = clear_tags(text)
    italian_freq = count_freq_of_words_in_text(italian_text)
    r = 1
    # exercise 1
    print("word, rank, freq, rank x freq")
    for k, v in italian_freq.items():
        print(f'{k}     {r}     {v}     {r * v} ')
        r += 1

    # exercise 2
    neighbours = get_neighbours(italian_text)
    for k, v in neighbours.items():
        print(k, len(set(v)), len(v))

    # exercise 3
    perc = percentage_of_language(italian_freq)
    for k, v in perc.items():
        if k < 60:
            print(f'{k}%', v)


if __name__ == "__main__":
    main()
