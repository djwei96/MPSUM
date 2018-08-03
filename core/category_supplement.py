from SPARQLWrapper import SPARQLWrapper, JSON

def extract_dbpeida_source_category_from_purl(subject_uri, predicate_uri):

    category_list = list()
    query_str = 'select distinct ?category where {'+'<'+subject_uri+'>'+' '+'<'+ predicate_uri+'> ?category}'
    #print(query_str)
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery(query_str)
    sparql.setReturnFormat(JSON)
    categories= sparql.query().convert()
    for category in categories['results']['bindings']:
        category_list.append(category['category']['value'])

    return category_list

def match_category_with_original_object(topic_word,obj_doc_list):

    for obj_dict in obj_doc_list:
        categories_list = obj_dict['categories']
        if len(categories_list) > 0 and topic_word in categories_list:
            topic_word = obj_dict['processed']

    return topic_word

def extract_yago_source_class_from_dbpedia(subject_uri):

    class_list = list()
    query_str = 'select distinct ?class ?x where {'+'<'+subject_uri+'>'+' ?class ?x}'
    #print(query_str)
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery(query_str)
    sparql.setReturnFormat(JSON)
    classes= sparql.query().convert()
    for class_uri in classes['results']['bindings']:
        #print(class_uri['x']['value'])
        class_list.append(class_uri['x']['value'])

    return class_list
