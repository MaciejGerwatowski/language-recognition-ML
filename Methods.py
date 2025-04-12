import os
import string
import Perceptron
from collections import Counter
def load_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    text = ''.join(lines).replace(" ", "").replace("\n", "").lower()

    test = sorted(text.split(" "))

    text = [char for char in text if 'a' <= char <= 'z']

    char_count = Counter(text)

    for letter in string.ascii_lowercase:
        if letter not in char_count:
            char_count[letter] = 0

    sum_char = sum(char_count.values())

    slownik = {}
    for i in char_count:
        slownik[i] = char_count[i]/ sum_char
    slownik = dict(sorted(slownik.items()))

    return list(slownik.values())


def load_text(text):
    text = text.replace(" ", "").replace("\n", "").lower()
    text = [char for char in text if 'a' <= char <= 'z']
    char_count = Counter(text)

    for letter in string.ascii_lowercase:
        if letter not in char_count:
            char_count[letter] = 0
    sum_char = sum(char_count.values())
    slownik = {}
    for i in char_count:
        slownik[i] = char_count[i] / sum_char
    slownik = dict(sorted(slownik.items()))

    return list(slownik.values())

def train_language(language, p):
    for file in os.listdir("./training_data/" + language):
        x = load_file("./training_data/" + language + "/" + file)
        p.learn(1, x)

    for dirr in os.listdir("./training_data/"):
        if dirr == language:
            continue
        path = f"./training_data/{dirr}"

        if not os.path.isdir(path):
            continue
        for file in os.listdir(path):
            x = load_file(path + "/" + file)
            p.learn(0, x)

def check_language(language, p):
    counter = 0
    for dirr in os.listdir("./training_data/"):
        d = 0
        if dirr == language:
            d = 1
        for file in os.listdir("./training_data/" + dirr):
            x = load_file("./training_data/" + dirr + "/" + file)
            if p.compute(x) == d:
                counter += 1
    return counter

def full_trained_perceptron(language):
    p = Perceptron.Perceptron(26, 0.001, 0.001)
    while check_language(language, p) < 60:
        train_language(language, p)
    return p


perceptrons = {
        full_trained_perceptron("Angielski") : "Angielski",
        full_trained_perceptron("Czeski") : "Czeski",
        full_trained_perceptron("Francuski") : "Francuski",
        full_trained_perceptron("Niemiecki") : "Niemiecki",
        full_trained_perceptron("Polski") : "Polski",
        full_trained_perceptron("Wloski") : "Wloski",
    }


def clasification(directory):

    answers = []
    for file in os.listdir(directory):
        x = load_file(directory + "/" + file)
        for p in perceptrons:
            if p.compute(x) == 1:
                print("Plik", file, "zakfalifikowano jako:", perceptrons[p])
                answers.append(perceptrons[p])
    return answers

def classify(text):
    tocompute = load_text(text)
    for p in perceptrons:
        if p.compute(tocompute) == 1:
            return f"wykryto język: {perceptrons[p]}"


def percentage_of_agreement(crr_ans, ans):
    crr_counter = Counter([x.lower() for x in crr_ans])
    ans_counter = Counter([x.lower() for x in ans])

    matches = 0
    for slowo in crr_counter:
        matches += min(crr_counter[slowo], ans_counter.get(slowo, 0))

    return matches / len(crr_ans) * 100 if crr_ans else 0.0