#!/bin/bash
val=100
python3 Q3.py "corpus.train" "corpus_prep.data" "patron.train.txt" $val
python3 Q3.py "corpus.dev" "corpus_prep.dev" "patron.train.txt" $val
python3 Q3.py "corpus.test" "corpus_prep.test" "patron.train.txt" $val
