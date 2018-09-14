#!/usr/bin/env python -tt

import random


def generate_trigram(words):
    if len(words) < 3:
        return
    for i in range(len(words) - 2):
        yield (words[i], words[i+1], words[i+2])

def generate_chain(data:list):
    chain = {}
    for line in data:
        words = 'BEGIN NOW {} END'.format(line).split()
        for word1, word2, word3 in generate_trigram(words):
            key = (word1, word2)
            if key in chain:
                chain[key].append(word3)
            else:
                chain[key] = [word3]
    return chain

def generate_text(chain):
    new_review = []
    sword1 = "BEGIN"
    sword2 = "NOW"

    while True:
        sword1, sword2 = sword2, random.choice(chain[(sword1, sword2)])
        if sword2 == "END":
            break
        new_review.append(sword2)

    result = ' '.join(new_review)
    return result



def generate_text_from_seed(chain, in_text=None):
    new_review = str(in_text).lower().split()

    if len(new_review) < 1 or (new_review[0] == 'None' and len(new_review) == 1):
        new_review = []
        sword1 = "BEGIN"
        sword2 = "NOW"
    elif len(new_review) == 1:
        sword1 = "NOW"
        sword2 = new_review[0]
    else:
        sword1 = new_review[-2]
        sword2 = new_review[-1]

    while True:
        try:
            try:
                sword1, sword2 = sword2, random.choice(chain[(sword1, sword2)])
            except:
                sword1 = "NOW"
                sword1, sword2 = sword2, random.choice(chain[(sword1, sword2)])
        except:
            print('didnt find that')
            sword2 = 'END'
        if sword2 == "END":
            break
        new_review.append(sword2)

    result = ' '.join(new_review)
    return result

def generate_n_text_from_seed(chain, in_text=None, n=5, max_char=None):
    out_list = []
    for i in range(n):
        text = generate_text_from_seed(chain, in_text=in_text)
        if max_char:
            text = text[:max_char-1]
        out_list.append(text)
    return out_list


# print(generate_n_text_from_seed(chain, in_text='what is ', max_char=100))