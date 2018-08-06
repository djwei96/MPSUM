# -*- coding: UTF-8 -*-
import os
import sys
import json
import rdf_preprocess_dict, rdf_preprocess_object, rdf_preprocess_predicate, category_supplement

'''
preprocess and supplement rdf triples:
If you want to supplement data from online database, please checkout our full edition brach.
or remove all json file and uncomment the following 3 comments.
Due to the mobility of online database, we can't gurantee the data you supplement are the same as we provide in this branch.
'''
#rdf_preprocess_dict.constructor()
#rdf_preprocess_object.constructor()
#rdf_preprocess_predicate.constructor()

#train model
import lda_train
rdf_preprocess_object.constructor()
lda_train.constructor()

#load object dictionary 
object_corpus_list_db = rdf_preprocess_object.retrieve_object_corpus_list('db')
object_corpus_list_lm = rdf_preprocess_object.retrieve_object_corpus_list('lm')

#load corpus_word
corpus_word_db = lda_train.retrieve_corpus_word('db')
corpus_word_lm = lda_train.retrieve_corpus_word('lm')

#rank triples for each file
def rank_rdf_triples(num, object_corpus_list, kb_path, corpus_word):

    topic_words = corpus_word[num] #topic words in current file
    targeted_words = [] #the targeted word in current file
    total_lines = [] #all triples in current file
    matched_total_lines = [] #triples which are already ranked
    predicate_list = [] #predicates which are already ranked

    #match topic words into targeted_words
    for topic_word in topic_words:
        topic_word = category_supplement.match_category_with_original_object(topic_word,object_corpus_list[num])
        for object_dict in object_corpus_list[num]:
                if topic_word == object_dict['processed']: 
                    targeted_words.append(object_dict['real']) 

    #read every triple in curerent into total_lines
    with open(kb_path[num], 'r', encoding=u'utf-8') as input_file: 
        for input_line in input_file:
            total_lines.append(input_line[:-1])

    #match targeted_word and total_lines
    for targeted_word in targeted_words:
        for current_line in total_lines:
            current_line_lower = str(current_line).lower()
            pred = rdf_preprocess_predicate.predicate_extract(current_line)
            pred_lower = pred.lower()
            if targeted_word in current_line_lower:
                if pred_lower in  predicate_list:
                    pass
                else:
                    predicate_list.append(pred_lower)
                    print(current_line)
                    matched_total_lines.append(current_line)
                    total_lines.remove(current_line)

    #MP algorithm 
    for current_line in total_lines:
        current_line_lower = str(current_line).lower()
        pred = rdf_preprocess_predicate.predicate_extract(current_line)
        pred_lower = pred.lower()
        if pred_lower in  predicate_list:
            pass
        else:
            predicate_list.append(pred_lower)
            print(current_line)
            matched_total_lines.append(current_line)
            total_lines.remove(current_line)


    for i in range(len(total_lines)):
        print(total_lines[i])
        matched_total_lines.append(total_lines[i])

    return matched_total_lines

#construct dirs for es_lda_output
def make_es_lda_output_subdir(kb_name, num, base_num, tfidf_flag):

    path_add = ''
    if tfidf_flag == True:
        path_add = '_with_tfidf'

    if not os.path.exists(os.path.join(rdf_preprocess_dict.rootdir, 'MPSUM_output'+path_add)):
        os.mkdir(os.path.join(rdf_preprocess_dict.rootdir, 'MPSUM_output'+path_add))
    es_lda_output_dir_path = os.path.join(rdf_preprocess_dict.rootdir, 'MPSUM_output'+path_add)
    
    if not os.path.exists(os.path.join(es_lda_output_dir_path, kb_name)):
        os.mkdir(os.path.join(es_lda_output_dir_path, kb_name))
        
    es_lda_output_dir_path_kb = os.path.join(es_lda_output_dir_path, kb_name)

    for i in range(base_num+1, base_num+num+1):
        if not os.path.exists(os.path.join(es_lda_output_dir_path_kb, str(i))):
            os.mkdir(os.path.join(es_lda_output_dir_path_kb, str(i)))

    return

def construct_es_lda_output(kb_name, num, base_num, matched_total_lines, tfidf_flag):

    num +=base_num

    path_add = ''
    if tfidf_flag == True:
        path_add = '_with_tfidf'

    es_lda_output_dir_path_kb = os.path.join(rdf_preprocess_dict.rootdir, 'MPSUM_output'+path_add, kb_name)

    with open(os.path.join(es_lda_output_dir_path_kb, str(num), str(num)+'_top5.nt'), 'w+', encoding=u'utf-8') as input_file:
        for i in range(5):
            input_file.write(matched_total_lines[i]+'\n')

    with open(os.path.join(es_lda_output_dir_path_kb, str(num), str(num)+'_top10.nt'), 'w+', encoding=u'utf-8') as input_file:
        for i in range(10):
            input_file.write(matched_total_lines[i]+'\n')

    with open(os.path.join(es_lda_output_dir_path_kb, str(num), str(num)+'_rank.nt'), 'w+', encoding=u'utf-8') as input_file:
        for line in matched_total_lines:
            input_file.write(line+'\n')

#construct results for knowlege base:dbpedia, lmdb
def entity_summarization(kb, kb_name, tfidf_flag):

    if kb == 'dbpedia':
        num, base_num = 100, 0
        kb_path = rdf_preprocess_dict.dbpedia_nt_path
        object_corpus_list = object_corpus_list_db
        corpus_word = corpus_word_db
    elif kb == 'lmdb':
        num, base_num = 40, 100
        kb_path = rdf_preprocess_dict.lmdb_nt_path
        object_corpus_list = object_corpus_list_lm
        corpus_word = corpus_word_lm
    else:
        return 

    make_es_lda_output_subdir(kb, num, base_num, tfidf_flag)

    for i in range(num):
        matched_total_lines = rank_rdf_triples(i, object_corpus_list, kb_path, corpus_word)
        construct_es_lda_output(kb, i+1, base_num, matched_total_lines, tfidf_flag)

    return 

if __name__ == '__main__':

    entity_summarization('dbpedia', 'db', False)
    entity_summarization('lmdb', 'lm', False)
      
    #flush buffer
    if os.path.exists(os.path.join(rdf_preprocess_dict.coredir, 'predicate_extract_temp.nt')):
        os.remove(os.path.join(rdf_preprocess_dict.coredir, 'predicate_extract_temp.nt'))