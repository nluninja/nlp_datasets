# re3d in CONLL format | Entity Extraction
This dataset is based on the re3d dataset, Relationship and Entity Extraction Evaluation Dataset, which has been cleaned and converted to CoNLL 2003 format.

The github project (https://github.com/dstl/re3d) README states:
<pre>
"This dataset was the output of a project carried out by Aleph Insights and
Committed Software on behalf of the Defence Science and Technology Laboratory
(Dstl). The project aimed to create a 'gold standard' dataset that could be
used to train and validate machine learning approaches to natural language
processing (NLP); specifically focusing on entity and relationship extraction
relevant to somebody operating in the role of a defence and security
intelligence analyst. The dataset was therefore constructed using documents
and structured schemas that were relevant to the defence and security analysis
domain."
</pre>
And:
<pre>
"The dataset comprised task-specific documents focused on the topic of the
conflict in Syria and Iraq;
The dataset included a range of source and document types, which had differing
levels of relevance to the overall ‘topic' of the dataset and possessed
differing entity densities (i.e. some documents containing a high concentration
of instances with others containing a lower concentration)"
</pre>

Each part of the dataset has its own license. For license information, see the
LICENSE file in each subdirectory.

## Entries
train: 19787  entries | test:  5501 entries

## URL
https://github.com/dstl/re3d

## File Format
text - CoNLL - IOB2

| Column | Description       |
| ----- | ------------------ |
|token | a string feature |
|ner_tag| a classification label, [22 classes](./data/classes.txt) |


## Example
<pre>
The	O
last	O
meeting	O
of	O
the	B-Organisation
Small	I-Organisation
Group	I-Organisation
took	O
place	O
in	O
Washington	B-Location
,	I-Location
D	I-Location
.	I-Location
C	I-Location
.	I-Location
</pre>
