# -*- coding: UTF-8 -*-
import os
import rdflib
import collections
import category_supplement
import json
import rdf_preprocess_dict

#predicate list in corpus
predicate_corpus_list_db = []
predicate_corpus_list_lm = []

#predicate set
predicate_set_db = set()
predicate_set_lm = set()

#construct predicate_doc_list
def form_predicate_doc_list(filepath):
    #usr rdflib to construct Graph and extract predicate
    g = rdflib.Graph()
    g.load(filepath, format='nt')

    #predicate list in current file
    predicate_doc_list = []

    #rdf preprocessor
    for pred in g.predicates():
        pred = predicate_preprocess(pred)
        #preprocess predicate
        predicate_doc_list.append(pred)

    return predicate_doc_list


#construct predicate_corpus_list
def form_predicate_corpus_list(predicate_corpus_list, filepath_list, num):
    
    for i in range(num):
        predicate_corpus_list.append(form_predicate_doc_list(filepath_list[i]))
    return 

#construct predicate_set
def form_and_store_predicate_set(predicate_doc_list_db, predicate_set, kb_name):
    
    for predicate_list in predicate_doc_list_db:
        for predicate in predicate_list:
            predicate_set.add(predicate)

    #usr json format to store predicate set
    with open(os.path.join(rdf_preprocess_dict.coredir,'predicate_corpus_list_'+kb_name+'.json'), 'w+', encoding='utf-8') as f:
        json.dump(list(predicate_set), f)

def predicate_preprocess(pred):
        
    pred = str(pred)
    pred = pred.lower() 

    #object extractor
    if '#' in pred: 
        pred = pred[pred.find('#')+1:]  
    else: 
        pred = pred[pred.rfind('/')+1:]
        if ':' in pred: 
            pred = pred[pred.find(':')+1:]
        
    return pred

#extractt single triple
def predicate_extract(triple):

    #using rdflib to construct Graph and extract predicate
    with open(os.path.join(rdf_preprocess_dict.coredir, 'predicate_extract_temp.nt'), 'w', encoding='utf-8') as extract_file:
        extract_file.write(triple)
    
    g = rdflib.Graph()
    g.load(os.path.join(rdf_preprocess_dict.coredir, 'predicate_extract_temp.nt'), format='nt')

    #rdf preprocesser
    for pred in g.predicates():
        pred = str(pred)
        pred = pred.lower() 
   
   #extract predicate
    if '#' in pred: 
        pred = pred[pred.find('#')+1:]  
    else: 
        pred = pred[pred.rfind('/')+1:]
        if ':' in pred: 
            pred = pred[pred.find(':')+1:]
        
    return pred

def constructor():

    form_predicate_corpus_list(predicate_corpus_list_db, rdf_preprocess_dict.dbpedia_nt_path, 100)
    form_predicate_corpus_list(predicate_corpus_list_lm, rdf_preprocess_dict.lmdb_nt_path, 40)

    form_and_store_predicate_set(predicate_corpus_list_db, predicate_set_db, 'db') 
    form_and_store_predicate_set(predicate_corpus_list_lm, predicate_set_lm, 'lm')

def retrieve_object_corpus_list(kb_name):

    with open(os.path.join(rdf_preprocess_dict.coredir,'predicate_corpus_list_'+kb_name+'.json'), 'r', encoding='utf-8') as f:
        predicate_corpus_list = json.load(f)
    
    return predicate_corpus_list

def load_predicate_set(kb_name):

    with open(os.path.join(rdf_preprocess_dict.coredir,'predicate_corpus_list_'+kb_name+'.json'), 'r', encoding='utf-8') as f:
        predicate_corpus_set = set(json.load(f))

    return predicate_corpus_set
    
if __name__ == '__main__':

    constructor()