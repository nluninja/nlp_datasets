# Georgetown University Multilayer Corpus for NER | Entity Extraction
## Description
The GUM corpus was collected and annotated at Georgetown University.  

For more information, see the [LICENSE](https://corpling.uis.georgetown.edu/gum),
and the following publication:
_Zeldes, Amir (2016) "The GUM Corpus: Creating Multilayer Resources in the
Classroom". Language Resources and Evaluation._  

This corpus version has been modified from the original one to focus on NER about a set of 22 classes, and transformed into IOB2/CoNLL like format.

## Entries
train: 44111  entries | test:  18236 entries

## URL
https://github.com/amir-zeldes/gum

## File Format
text - CoNLL - IOB2

| Column | Description       |
| ----- | ------------------ |
|token | a string feature |
|ner_tag| a classification label, [23 classes](./data/classes.txt) |


## Example
<pre>
    Pacific	B-person
    Standard	I-person
    owner	I-person
    ,	O
    Jonathan	B-person
    M.	I-person
    Stan	I-person
    ,	O
    displays	O
    the	O
    Santorum	B-substance
    cocktail	I-substance
    drink	I-substance
    as	O
    a	B-object
    finished	I-object
    product	I-object
</pre>