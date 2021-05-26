# CONLL 2003 - Named Entity Extraction
## Description

CoNLL-2003 dataset has been designed for language-independent named entity recognition. The dataset provides token level annotation for pos, chunks and named entities. The original data files have -DOCSTART- lines used to separate documents, but these lines are removed here. Indeed -DOCSTART- is a special line that acts as a boundary between two different documents, and it is filtered out in this implementation.  

## Entries
train 14041 | test 3250 | valid 3453  

## URL
https://www.aclweb.org/anthology/W03-0419/

## File Format
text - CoNLL 2003 - IOB2

| Column | Description        |
| ----- | ------------------ |
|id | a string feature. |
|tokens | a list of string features. |
| pos_tags | a list of classification labels, with possible values including " (0), '' (1), # (2), $ (3), ( (4). |
| chunk_tags| a list of classification labels, with possible values including O (0), B-ADJP (1), I-ADJP (2), B-ADVP (3), I-ADVP (4). |
|ner_tags| a list of classification labels, with possible values including O (0), B-PER (1), I-PER (2), B-ORG (3), I-ORG (4). |

## Example 
<pre>
   U.N.         NNP  I-NP  I-ORG 
   official     NN   I-NP  O 
   Ekeus        NNP  I-NP  I-PER 
   heads        VBZ  I-VP  O 
   for          IN   I-PP  O 
   Baghdad      NNP  I-NP  I-LOC 
   .            .    O     O
</pre>
