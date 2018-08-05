# MPSUM: Predicate-Based Matching for RDF Triples with Application to LDA<br>
-----
-----
This project aims at generating brief but representative summaries for entities
## Contirbutors and background
### Contributors
- [Dongjun Wei](weidongjun123@gmail.com)<br>
- [Shiyuan Gao](gsyuan12@163.com)<br> 
- [Yaxin Liu](crayou_liu@163.com)<br>
- [Zhibing Liu](liuzhbing1996@163.com)<br> 
- [Longtao Huang](huanglongtao@iie.ac.cn)<br>
### Background
This is a souce code and output for **[Entity Summarization](http://ws.nju.edu.cn/summarization/esbm/)***(top5, top10, all)* in **dbpedia** and **ldmb**.<br>
The paper of this porject is in Proceedings of 1st International Workshop on EntitY REtrieval, Lingotto, Turin, Italy, 22 October 2018 (EYRE’18), 4 pages.<br>
If you have any questions or suggestions, please feel free to contact the contirbutors mentioned above.<br>
## Structure
The directory structure of these files should be as follows.
```
|--MPSUM
	|--core
		|-- rdf_preprocess_dict.py
		|-- category_supplement.py
		|-- ...
		|--- lda_test_and_output.py
	|-- dbpedia
		|-- 1
			|-- 1_top5.nt
			|-- 1_top10.nt
			|-- 1_rank.nt
		|-- 2
		|-- ...
		|-- 100
  	|-- lmdb
		|-- 101
			|-- 101_top5.nt
			|-- 101_top10.nt
			|-- 101_rank.nt
		|-- 102
		|-- ...
		|-- 140
	|--MPSUM_output
		|-- dbpedia
			|-- 1
				|-- 1_top5.nt
				|-- 1_top10.nt
				|-- 1_rank.nt
			|-- 2
			|-- ...
			|-- 100
  		|-- lmdb
			|-- 101
				|-- 101_top5.nt
				|-- 101_top10.nt
				|-- 101_rank.nt
			|-- 102
			|-- ...
			|-- 140
		
```
- **core:** *This direcotry is the main body of our project, includes:*<br>
  **Konwledge Base preprocessor** *(rdf_preprocess_dict.py, rdf_preprocess_object.py, rdf_preprocess_predicate.py)*<br>
  **Category Supplementor** *(category_supplement.py)*<br>
  **Data for MPSUM in json fomat** *(object_corpus_list_db.json, etc)*<br>
  **dbpedia and lmdb:** *The dataset(Knowledge Base for our Entiry Summarization)*<br>
  **MPSUM_output:** *The output of Entity Summarization using our MPSUM model(Tips: You can remove this directory before running our project, and you can see this directory after the end of running our project as the output. The details about how to run our project will be dicussed below.)*<br>
## Coding Environment

-----
	Ubuntu 16.04
	python3.6 (modules: rdflib, sklearn, lda)
	vscode
-----

## Usage

----- 
The usage of this Entity Summarization follow these steps:

```linux
git clone git@github.com:WeiDongjunGabriel/MPSUM.git
cd MPSUM
cd core
python lda_test_and_output.py
```
