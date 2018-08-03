# -*- coding: UTF-8 -*-
import json 
import os
import rdf_preprocess_dict

object_corpus_list_db = []
object_corpus_list_lm = []

def retrieve_object_corpus_list(kb_name):
    with open(os.path.join(rdf_preprocess_dict.coredir,'object_corpus_list_'+kb_name+'.json'), 'r', encoding='utf-8') as f:
        object_corpus_list = json.load(f)
    return object_corpus_list


def output_object_corpus_list(kb_name, object_corpus_list):

    output_path_name = os.path.join(rdf_preprocess_dict.coredir, 'object_output_'+kb_name+'.txt')
    
    with open(output_path_name, 'w+', encoding='utf-8') as f:
        for doc in object_corpus_list:
            for dictionary in doc:
                f.writelines(dictionary['processed']+' ')
                for i in range(len(dictionary['categories'])):
                    f.writelines(dictionary['processed']+' ')
                    f.writelines(dictionary['categories'][i]+' ')
            f.write('\n')

def object_preprocess(obj):
    
    return rdf_preprocess_dict.object_compact(rdf_preprocess_dict.object_extract(obj))

def constructor():

    output_object_corpus_list('db', retrieve_object_corpus_list('db'))             
    output_object_corpus_list('lm', retrieve_object_corpus_list('lm'))

if __name__ == '__main__':

    constructor()
