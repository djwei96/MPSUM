# -*- coding: UTF-8 -*-
import os
import rdflib
import collections
import category_supplement
import json
import string

# main path 
rootdir = os.path.normpath(os.path.dirname(os.path.dirname(__file__))) #root path
coredir = os.path.join(rootdir, 'core') #core path 
dbpediadir = os.path.join(rootdir, 'dbpedia') #dbpedia path 
lmdbdir = os.path.join(rootdir, 'lmdb') #lmdb path

#paths in dbpedia
dbpedia_nt_path = []
for i in range(1, 101):
    dbpedia_nt_path.append(os.path.join(dbpediadir,str(i),str(i)+'_desc.nt')) 

#paths in lmdb
lmdb_nt_path = []
for i in range(101, 141):
    lmdb_nt_path.append(os.path.join(lmdbdir,str(i),str(i)+'_desc.nt')) 

object_corpus_list_db = []
object_corpus_list_lm = []

#extract object
def object_extract(obj):
        
    obj = str(obj)
    obj = obj.lower() 

   # object extractor
    if '#' in obj: 
        obj = obj[obj.find('#')+1:]  
    else: 
        obj = obj[obj.rfind('/')+1:]
        if ':' in obj: 
            obj = obj[obj.find(':')+1:]
        
    return obj

#object compactor
def object_compact(obj):

    obj = obj.translate(str.maketrans('', '', string.punctuation))
    if ' ' in obj:
        obj = obj.replace(' ', '') 
    
    return obj

#category extractor
def add_category_from_dbpeida(subject_uri):
    predicate_uri = 'http://purl.org/dc/terms/subject'
    category_list = []
    #if 'http://dbpedia.org/resource/' in subject_uri:
    category_list = category_supplement.extract_dbpeida_source_category_from_purl(subject_uri, predicate_uri) 
    category_list = [object_compact(object_extract(x)) for x in category_list]
    print(category_list)
    return category_list

def add_class_from_dbpedia(subject_uri):

    #if 'http://dbpedia.org/class/yago/' in subject_uri:
    class_list = category_supplement.extract_yago_source_class_from_dbpedia(subject_uri) 
    class_list = [object_compact(object_extract(x)) for x in class_list]
    print(class_list)
    return class_list

def data_supplier(subject_uri):

    supply_list = []
    if 'http://dbpedia.org/resource/' in subject_uri:
        supply_list = add_category_from_dbpeida(subject_uri)
    #elif 'http://dbpedia.org/class/yago/' in subject_uri:
    #    supply_list = add_class_from_dbpedia(subject_uri)
    else:
        pass
    
    return supply_list

def form_object_doc_list(filepath):

    g = rdflib.Graph()
    g.load(filepath, format='nt')

    object_doc_list = []

    for obj in g.objects():
        object_dictionary = {'real':'', 'processed':'', 'categories':[]}
        object_dictionary['categories'] = data_supplier(str(obj))
        obj = object_extract(obj)
        object_dictionary['real'] = obj
        object_dictionary['processed'] = object_compact(obj)
        object_doc_list.append(object_dictionary)

    return object_doc_list

def form_and_store_object_corpus_list(kb_name='db', kb_nt_path_list=dbpedia_nt_path, base_num=0, num=100):

    object_corpus_list = []
    for i in range(num):
        object_corpus_list.append(form_object_doc_list(kb_nt_path_list[i]))
    
    with open(os.path.join(coredir,'object_corpus_list_'+kb_name+'.json'), 'w+', encoding='utf-8') as f:
        json.dump(object_corpus_list, f)

    return 

def constructor():

    form_and_store_object_corpus_list()
    form_and_store_object_corpus_list('lm', lmdb_nt_path, 100, 40)

if __name__ == '__main__': 

    constructor()
