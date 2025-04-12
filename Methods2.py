import os

import Methods
import Perceptron2
from Methods import load_text


def train_language2(language, p):
    for file in os.listdir("./training_data/" + language):
        x = Methods.load_file("./training_data/" + language + "/" + file)
        p.learn(1, x)

    for dirr in os.listdir("./training_data/"):
        if dirr == language:
            continue
        path = f"./training_data/{dirr}"

        if not os.path.isdir(path):
            continue
        for file in os.listdir(path):
            x = Methods.load_file(path + "/" + file)
            p.learn(-1, x)


def check_error(language, p):
    res =0
    for dirr in os.listdir("./training_data/"):
        d = -1
        if dirr == language:
            d = 1
        for file in os.listdir("./training_data/" + dirr):
            x = Methods.load_file("./training_data/" + dirr + "/" + file)
            res += 0.5 * (d - p.compute(x))**2
    return res

def full_trained_perceptron2(language, tresh):
    p = Perceptron2.Perceptron2(26, 0.01)
    max_epok = 1000;
    c = 0
    while c < max_epok:
        c += 1
        should_break = False
        for dirr in os.listdir("./training_data/"):
            d = -1
            if dirr == language:
                d = 1
            for file in os.listdir("./training_data/" + dirr):
                x = Methods.load_file("./training_data/" + dirr + "/" + file)
                error = 0.5 * (d - p.compute(x))**2
                if error > tresh:
                    if dirr == language:
                        p.learn(d, x)
                else:
                    should_break = True
                    break
            if should_break:
                break
        if should_break:
            break
    return p

tresh = 0.01
perceptrons2 = {
        full_trained_perceptron2("Angielski", tresh) : "Angielski",
        full_trained_perceptron2("Czeski", tresh) : "Czeski",
        full_trained_perceptron2("Francuski", tresh) : "Francuski",
        full_trained_perceptron2("Niemiecki", tresh) : "Niemiecki",
        full_trained_perceptron2("Polski", tresh) : "Polski",
        full_trained_perceptron2("Wloski", tresh) : "Wloski",
    }


def classify2(text):
    tocompute = Methods.load_text(text)
    res = {}
    for p, language in perceptrons2.items():
        y = p.compute(tocompute)
        res[language] = y
    return max(res, key=res.get)

def clasification2(directory):
    answers = []
    for file in os.listdir(directory):
        res = {}
        for p , language in perceptrons2.items():
            y = p.compute(Methods.load_file(directory + "/" + file))
            res[language] = y
        answers.append(max(res, key=res.get))
    #print(answers, len(answers))
    return answers