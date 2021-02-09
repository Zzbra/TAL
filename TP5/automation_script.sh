#!/bin/bash
val=412
python3 Q3_4.py "corpus.data" "corpus_prep.data" "patron.train.txt" $val
python3 Q3_4.py "corpus.dev" "corpus_prep.dev" "patron.train.txt" $val
#python3 Q3.py "corpus.test" "corpus_prep.test" "patron.train.txt" $val
