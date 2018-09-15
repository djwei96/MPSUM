# MPSUM: Predicate-Based Matching for RDF Triples with Application to LDA<br>
This project aims at generating brief but representative summaries for entities in **dbpedia** and **lmdb**.<br>
## CONTRIBUTORS AND BACKGROUND
### Contributors
All of the contributors in this project work in the Institute of Information Enginerring CAS, our name and E-mail address are as follows.<br>
If you have any questions or suggestions, please do not hesitate to contact us.<br>
#### Tutor
- **[Longtao Huang](http://people.ucas.edu.cn/~huanglongtao):** huanglongtao@iie.ac.cn<br>
#### Students
- **Dongjun Wei:** weidongjun123@gmail.com<br>
- **Shiyuan Gao:** gsyuan12@163.com<br> 
- **Yaxin Liu:** crayou_liu@163.com<br>
- **Zhibing Liu:** liuzhbing1996@163.com<br> 
### Background
This project contains souce code and output for **[Entity Summarization](http://ws.nju.edu.cn/summarization/esbm/)***(top5, top10, all)* in **[dbpedia](https://wiki.dbpedia.org/)** and **[lmdb](http://symas.com/lmdb)**. Compared with the results shown in the [official website](http://ws.nju.edu.cn/summarization/esbm/), We have achieved state-of-the-art results.<br>
The paper of this porject is accepted by the 1st International Workshop on EntitY REtrieval, Lingotto, Turin, Italy, 22 October 2018 (EYRE’18), 4 pages.<br>
This brach is the full edition without pre-store data in json format acquired from the online [database](https://wiki.dbpedia.org/).<br>
## STRUCTURE AND EXPLANATOIN
### Structure
The directory structure of our projects should be as follows.
```
|-- MPSUM
	|--core
		|-- rdf_preprocess_dict.py
		|-- category_supplement.py
		|-- ...
		|-- lda_test_and_output.py
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
### Explanation
- **[core](./core):** This direcotry is the main body of our project, includes:<br>
     - **Konwledge Base preprocessor** (*rdf_preprocess_dict.py, rdf_preprocess_object.py, rdf_preprocess_predicate.py*)<br>
     - **Category Supplementor** (*category_supplement.py*)<br>
     - **Data for MPSUM in json fomat** (*object_corpus_list_db.json, etc*)<br>
- **[dbpedia](./dbpedia) and [lmdb](./lmdb):** The dataset(Knowledge Base) used in our Entiry Summarization<br>
## ENVIRONMENT AND DEPENDENCY
### Environment

- Ubuntu 16.04
- python 3.6 
- git
- VSCODE 1.25(optional)

### Dendency
Several python modules are required in our project as follows:
```python
pip3 install sklearn
pip3 install lda
pip3 install SPARQLWrapper
pip3 install rdflib
```
## USAGE
```linux
git clone git@github.com:WeiDongjunGabriel/MPSUM.git
```
Before running this project, please remove the [MPSUM_output](./MPSUM_output) directory for your own output. The MPSUM_output we provide is for the workshop mentioned above to verify and evaluate our output.
### Terminal 
if you use terminal to run our project, please follow these steps:
```linux
cd MPSUM
cd core 
python lda_test_and_output.py
```
### VSCODE
if you use VSCODE as your IDE, please follow these steps:
1. open the MPSUM folder with your VSCODE
2. open the python file named "lda_test_output.py"
3. run this python file in your VSCODE
## OUTPUT AND EVALUATION
### Output
The output is in the folder named "MPSUM_output" as your running this project with the above steps.
### Evaluation
You can evaluate your own output's F-measure and MAP by following instructions in [ESBM Benchmark](http://ws.nju.edu.cn/summarization/esbm/).
## ACKNOWLEDGEMENT
This is our Summer internship project in IIE, my tutor [Longtao Huang](http://people.ucas.edu.cn/~huanglongtao) and group members has helped me a lot. Without them, I am certainly unable to complete this project.<br> 
