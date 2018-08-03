# -*- coding: UTF-8 -*-
import os
import rdflib
import collections
import category_supplement
import json
import rdf_preprocess_dict

#所有predicate组成的二维list
predicate_corpus_list_db = []
predicate_corpus_list_lm = []

#所有predicate组成的集合
predicate_set_db = set()
predicate_set_lm = set()

#构建各文件中的predicate_doc_list
def form_predicate_doc_list(filepath):
    #利用rdflib建立Graph并提取predicate
    g = rdflib.Graph()
    g.load(filepath, format='nt')

    #该文件predicate组成的list
    predicate_doc_list = []

    #rdf预处理
    for pred in g.predicates():
        pred = predicate_preprocess(pred)
        #处理predicate
        predicate_doc_list.append(pred)

    return predicate_doc_list


#构建各文件中的predicate_corpus_list
def form_predicate_corpus_list(predicate_corpus_list, filepath_list, num):
    
    for i in range(num):
        predicate_corpus_list.append(form_predicate_doc_list(filepath_list[i]))
    return 

#构建各KB中的predicate_set
def form_and_store_predicate_set(predicate_doc_list_db, predicate_set, kb_name):
    
    for predicate_list in predicate_doc_list_db:
        for predicate in predicate_list:
            predicate_set.add(predicate)

    #json格式无法保存set数据类型，故将其转换为list存储
    with open(os.path.join(rdf_preprocess_dict.coredir,'predicate_corpus_list_'+kb_name+'.json'), 'w+', encoding='utf-8') as f:
        json.dump(list(predicate_set), f)
        #print(len(predicate_set))

def predicate_preprocess(pred):
        
    pred = str(pred)
    pred = pred.lower() #将提取object全部处理为小写

    #提取object
    if '#' in pred: 
        pred = pred[pred.find('#')+1:]  
    else: 
        pred = pred[pred.rfind('/')+1:]
        if ':' in pred: 
            pred = pred[pred.find(':')+1:]
        
    return pred

#提取单一triple中的prediate
def predicate_extract(triple):

    #利用rdflib建立Graph并提取predicate
    with open(os.path.join(rdf_preprocess_dict.coredir, 'predicate_extract_temp.nt'), 'w', encoding='utf-8') as extract_file:
        extract_file.write(triple)
    
    g = rdflib.Graph()
    g.load(os.path.join(rdf_preprocess_dict.coredir, 'predicate_extract_temp.nt'), format='nt')

    #rdf预处理 
    for pred in g.predicates():
        pred = str(pred)
        pred = pred.lower() #将提取predicate全部处理为小写
   
   #提出predicate
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



