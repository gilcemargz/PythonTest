from newspaper import Article
import random
import string
import nltk
# import numpy as np
import warnings
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
warnings.filterwarnings("ignore")

# nltk.download("punkt")


def greeting_response(text: string):
    text = text.lower()

    bot_greetings = ['oi', 'olá', 'como vai?', 'em que posso ajudar']
    user_greetins = ['bom dia', 'boa tarde', 'boa noite', 'ola', 'ajuda']

    for word in text.split():
        if word in user_greetins:
            return random.choice(bot_greetings)


def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))

    x = list_var
    for i in range(length):
        for j in range(length):
            if x[list_index[i]] > x[list_index[j]]:
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp

    return list_index


article = Article(
    "https://www.mayoclinic.org/diseases-conditions/chronic-kidney-disease/symptoms-causes/syc-20354521")
article.download()
article.parse()
article.nlp()
corpus = article.text

# print(corpus)

text = corpus
sentence_list = nltk.sent_tokenize(text)

"""
l = 0
for x in sentence_list:
    print(str(l) + ' ' + x)
    l = l + 1
"""


def bot_response(user_input: string):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response = ''
    print(len(sentence_list))
    cm = CountVectorizer().fit_transform(sentence_list)
    # print(*sentence_list, sep="\n")
    similarity_scores = cosine_similarity(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten()
    # print(similarity_scores_list)
    index = index_sort(similarity_scores_list)
    index = index[1:]
    # print(index)
    response_flag = 0

    j = 0
    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0:
            bot_response = bot_response + ' ' + sentence_list[index[i]]
            response_flag = 1
            j = j + 1
            if j > 2:
                break

    if response_flag == 0:
        bot_response = bot_response + ' ' + 'Não sei do que você está falando.'

    sentence_list.remove(user_input)

    return bot_response


print("Olá, sou um robô eu vou te ajudar. "
      "Para encerrar nossa conversa digite: Tchau")

while True:
    duvida = input()
    if duvida.lower() == "tchau":
        break

    if greeting_response(duvida) != None:
        print('Robô:' + greeting_response(duvida))
    else:
        print("Robô:" + bot_response(duvida))
