# MPSUM: Predicate-Based Matching for RDF Triples with Application to LDA<br>
EYRE@CIKM'18 paper: "[MPSUM: Predicate-Based Matching for RDF Triples with Application to LDA](https://arxiv.org/pdf/1905.10625.pdf)"
## ENVIRONMENT AND DEPENDENCY
### Environment

- Ubuntu 16.04
- python 3.6 

### Dependency
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
Before running this project, please remove the **[MPSUM_output](./MPSUM_output)** directory for your own output. The MPSUM_output we provide is for the workshop mentioned above to verify and evaluate our output.
## OUTPUT AND EVALUATION
### Output
The output is in the folder named "MPSUM_output" as your running this project with the above steps.
### Evaluation
You can evaluate your own output's F-measure and MAP by following instructions in [ESBM Benchmark](http://ws.nju.edu.cn/summarization/esbm/).
## CITATION
If you use our model or code, please kindly cite as follows:
```
@inproceedings{MPSUM,
  author    = {Dongjun Wei and
  	       Shiyuan Gao and
               Yaxin Liu and
               Zhibing Liu and
               Longtao Huang and 
               Songlin Hu},
  title     = {MPSUM: Predicate-Based Matching for RDF Triples with Application to LDA},
  booktitle = {EYRE@CIKM},
  year      = {2018}
}
```
