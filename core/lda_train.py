# -*- coding: UTF-8 -*-
import os
import json
import rdf_preprocess_dict, rdf_preprocess_object, rdf_preprocess_predicate
import lda
import numpy as np
import rdflib
from sklearn import feature_extraction   
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import HashingVectorizer 
import json

object_corpus_list_db = rdf_preprocess_object.retrieve_object_corpus_list('db')
object_corpus_list_lm = rdf_preprocess_object.retrieve_object_corpus_list('lm')

def apply_lda_model(kb_name, num, n_top_words):

    texts = []
    corpus_word = []

    with open(os.path.join(rdf_preprocess_dict.coredir, 'object_output_'+kb_name+'.txt'), encoding='utf-8') as train_file:
        for line in train_file:
            texts.append(line[:-1])

    vectorizer = CountVectorizer()
 
    doc_term_matrix = vectorizer.fit_transform(texts)
    texts_object = vectorizer.get_feature_names()

    n_topics = len(rdf_preprocess_predicate.load_predicate_set(kb_name))
    if kb_name == 'db':
        model = lda.LDA(n_topics=n_topics, n_iter=1500, alpha=5/n_topics, refresh=100)
    elif kb_name == 'lm':
        model = lda.LDA(n_topics=n_topics, n_iter=1500, alpha=2/n_topics, eta=50/n_topics, refresh=100)
    else:
        return 
    model.fit(doc_term_matrix)  

    vocab = model.topic_word_

    doc_topic = model.doc_topic_

    for i in range(num):

        top_topic_num = doc_topic[i].argmax()
        topic_words = np.array(texts_object)[np.argsort(vocab[top_topic_num])][:-(n_top_words+1):-1] 
        topic_words_list = [word for word in topic_words]
        corpus_word.append(topic_words_list)
    
    return corpus_word

def form_and_store_corpus_word(kb_name, num, n_top_words):

    corpus_word = apply_lda_model(kb_name, num, n_top_words)

    with open(os.path.join(rdf_preprocess_dict.coredir,'corpus_word_'+kb_name+'.json'), 'w+', encoding='utf-8') as f:
        json.dump(corpus_word,  f)

def retrieve_corpus_word(kb_name):

    with open(os.path.join(rdf_preprocess_dict.coredir,'corpus_word_'+kb_name+'.json'), 'r', encoding='utf-8') as f:
        corpus_word = json.load(f)

    return corpus_word

def constructor():

    n_topic_words = 3000
    form_and_store_corpus_word('db', 100, n_topic_words)
    form_and_store_corpus_word('lm', 40, n_topic_words)

if __name__ == '__main__':

    n_topic_words = 3000
    form_and_store_corpus_word('db', 100, n_topic_words)
    form_and_store_corpus_word('lm', 40, n_topic_words)
