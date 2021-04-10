# CONLL 2003 - Named Entity Extraction

format: text - CONLL 2003
Entries:  

## Format
| Colum | Description        |
| ----- | ------------------ |
|id | a string feature. |
|tokens | a list of string features. |
| pos_tags | a list of classification labels, with possible values including " (0), '' (1), # (2), $ (3), ( (4). |
| chunk_tags| a list of classification labels, with possible values including O (0), B-ADJP (1), I-ADJP (2), B-ADVP (3), I-ADVP (4). |
|ner_tags| a list of classification labels, with possible values including O (0), B-PER (1), I-PER (2), B-ORG (3), I-ORG (4). |

### Example 

`U.N.         NNP  I-NP  I-ORG 
   official     NN   I-NP  O 
   Ekeus        NNP  I-NP  I-PER 
   heads        VBZ  I-VP  O 
   for          IN   I-PP  O 
   Baghdad      NNP  I-NP  I-LOC 
   .            .    O     O 
`
