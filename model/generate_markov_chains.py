from generate_trigrams import generate_chain, generate_text, generate_n_text_from_seed, generate_text_from_seed
import pickle
import pandas as pd
# from keras.utils.data_utils import get_file
import json
# import io
import re

# Trump
with open('./model/data/trump_tweets.json') as f:
    tweet_data = json.load(f)

in_list = []
for line in tweet_data:
    in_list.append(line['text'].lower())

chain = generate_chain(in_list)
pickle.dump(chain, open("./model/chains/trump.p", "wb" ))

print(generate_text(chain))
print(generate_text_from_seed(chain, in_text='what is '))

# Seinfeld

in_df = pd.read_csv('./model/data/clean_scripts.csv')
in_df['dialogue_clean'] = in_df['dialogue_clean'].str.lower()

filter_df = in_df[in_df['speaker'] == 'JERRY:']
in_list = list(filter_df.dialogue_clean)
chain = generate_chain(in_list)
pickle.dump(chain, open("./model/chains/jerry.p", "wb" ))

print('JERRY')
print(generate_text(chain))
print(generate_text_from_seed(chain, in_text='what is '))

# George

filter_df = in_df[in_df['speaker'] == 'GEORGE:']
in_list = list(filter_df.dialogue_clean)
chain = generate_chain(in_list)
pickle.dump(chain, open("./model/chains/george.p", "wb" ))

print('GEORGE')
print(generate_text(chain))
print(generate_text_from_seed(chain, in_text='what is '))

# Elaine

filter_df = in_df[in_df['speaker'] == 'ELAINE:']
in_list = list(filter_df.dialogue_clean)
chain = generate_chain(in_list)
pickle.dump(chain, open("./model/chains/elaine.p", "wb" ))

print('ELAINE')
print(generate_text(chain))
print(generate_text_from_seed(chain, in_text='what is '))

# Kramer
filter_df = in_df[in_df['speaker'] == 'KRAMER:']
in_list = list(filter_df.dialogue_clean)
chain = generate_chain(in_list)
pickle.dump(chain, open("./model/chains/kramer.p", "wb" ))

print('KRAMER')
print(generate_text(chain))
print(generate_text_from_seed(chain, in_text='what is '))


# Newman
filter_df = in_df[in_df['speaker'] == 'NEWMAN:']
in_list = list(filter_df.dialogue_clean)
chain = generate_chain(in_list)
pickle.dump(chain, open("./model/chains/newman.p", "wb" ))

print('NEWMAN')
print(generate_text(chain))
print(generate_text_from_seed(chain, in_text='what is '))

# Nietzsche

with open('./model/data/nietzsche.txt', 'r') as f:
    text = f.read()

text_list = re.split('([!.?;]+)', text)

text_list = [re.sub('[!.?;]', '', x) for x in text_list]

text_list = [re.sub('\s+', ' ', x).strip() for x in text_list]

text_list = [x for x in text_list if x != '']


chain = generate_chain(text_list)
pickle.dump(chain, open("./model/chains/nietzsche.p", "wb" ))


print('NIETZSCHE:')
print(generate_text(chain))
print(generate_text_from_seed(chain, in_text='what is '))