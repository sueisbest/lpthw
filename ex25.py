# -*- coding:utf-8 -*-

from sys import argv
import codecs

def break_words(stuff):
    words = stuff.split(' ')
    return words
#I love Shanghai best

def sort_words(words):
    return sorted(words)

def print_first_word(words):
    word = words.pop(0)
    print(word)
    print(words)

def print_last_word(words):
    word = words.pop(-1)
    print(word)
    print(words)

def sort_sentence(sentence):
    words = break_words(sentence)
    return  sort_words(words)

def print_first_and_last(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

a = break_words('I love Alpha prefer to Shanghai')
print(a)