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
    return sort_words(words)

def print_first_and_last(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

'''
ais= break_words('I love Alpha prefer to Shanghai')
print(ais)
bs = sort_words(ais)
print(bs)
# print(ais)
print_first_word(bs)
# print(bs)
# ais没变, bs变了.
print_last_word(ais)
cs = sort_sentence('I love Alpha prefer to Shanghai')
print(cs)
print_first_and_last('I love Alpha prefer to Shanghai')
'''

script, filename = argv
fh = codecs.open(filename,'r',encoding='utf-8')
sentence1 = fh.readline()
fh.close()

print(sentence1)
bs = sort_words(break_words(sentence1))
print(bs)
# print(ais)
print_first_word(bs)
# print(bs)
# ais没变, bs变了.
print_last_word(break_words(sentence1))
cs = sort_sentence('I love Alpha prefer to Shanghai')
print(cs)
print_first_and_last('I love Alpha prefer to Shanghai')
