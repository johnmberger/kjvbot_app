from collections import defaultdict
from itertools import tee
from random import choice
import re
from nltk.tokenize import sent_tokenize

def nwise(iterable, n=2):
        if len(iterable) < n:
            return
        iterables = tee(iterable, n)
        for i, iter_ in enumerate(iterables):
            for num in range(i):
                next(iter_)
        return zip(*iterables)

def build_sentence(seed, sent_tokens):

    token = ''
    
    while token not in set('.?!'):
        last_tokens = tuple(seed[-3:])
        new_token = choice(sent_tokens[last_tokens])
        seed.append(new_token)
        token = new_token
    
    sentence = ' '.join(seed)
    sentence = re.sub(r'\s+([.,?!])',r'\1', sentence)
        
    return sentence

def markovize(word1, word2, word3, fileid, char_limit=None):   
    
    with open('/Users/timothybeal/workspace/Flask_tutorial/src/kjvbot_app/' + fileid, encoding='utf-8') as f:
        text = f.read()
    
    sentences = sent_tokenize(text)
    sent_tokens = defaultdict(list)
    for sentence in sentences:
        tokens = re.findall(r"[\w']+|[.,?!]", sentence)
        nwise_ = nwise(tokens, n=4)
        if nwise_:
            for token1, token2, token3, token4 in nwise_:
                sent_tokens[token1, token2, token3].append(token4)
    
    too_long = True
    
    while too_long:
        sentence = [word1, word2, word3]
    
        utterance = build_sentence(sentence, sent_tokens)
        len_utterance = len(utterance)
         
        if char_limit != None and len_utterance > char_limit:
            too_long = True
        else:
            too_long = False
            
    return utterance
         
