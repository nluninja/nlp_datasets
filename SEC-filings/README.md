# SEC Filings - Named Entity Extraction
## Description
The dataset is generated using CoNll2003 data and financial documents obtained
from U.S. Security and Exchange Commission (SEC) filings.

## Entries
train: 41010 entries  | test:  13246 entries

## URL / Attibution

This dataset is made available under the terms of the Creative Commons
Attribution 3.0 Unported licence
(http://creativecommons.org/licenses/by/3.0/), with attribution via citation
of the following paper, which describes the dataset in full detail:

Julio Cesar Salinas Alvarado, Karin Verspoor and Timothy Baldwin (2015) Domain
Adaption of Named Entity Recognition to Support Credit Risk Assessment, In
Proceedings of 13th annual workshop of The Australasian Language Technology
Association, Sydney, Australia.

## File Format
IOB2 

| Column | Description        |
| ----- | ------------------ |
|id | a string feature. |
| chunk label | a classification label for named entity |
| - | empty column|
|ner_tags| a classification label for named entity|


| Labels |
| ------ |
|PER
|LOC
|ORG
|MISC|

## Example
<pre>
-DOCSTART- -X- O O

Subordinated NNP - O
Loan NNP - O
Agreement NNP - O
- : - O
Silicium NNP - I-ORG
</pre>