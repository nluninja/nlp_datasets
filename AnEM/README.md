# The Anatomical Entity Mention (AnEM) corpus - Named Entity Extraction
## Description
The abstracts contained in the corpus are from PubMed, a database of
the U.S. National Library of Medicine (NLM). Please see the NLM page
on copyright information regarding the copyright of the abstracts:
http://www.nlm.nih.gov/databases/download.html

The full text extracts contained in the corpus are from articles in
the Open Access Subset of the PubMed Central (PMC) database of the
NLM. These articles are made available under a Creative Commons or
similar license. Please see the REFERENCES file in this distribution
for references to the articles and the PMC version of each article for
the specific license terms.

This dataset consists of abstracts and full-text biomedical papers.
It was downloaded in November 2017 from:

http://www.nactem.ac.uk/anatomy/

Specifically:

http://www.nactem.ac.uk/anatomy/data/AnEM-1.0.4.tar.gz


## Entries
train: 71697 entries  | test:  45939 entries

## URL / Attibution

Tomoko Ohta, Sampo Pyysalo, Jun'ichi Tsujii and Sophia Ananiadou (2012).
Open-domain Anatomical Entity Mention Detection. In Proceedings of ACL 2012
Workshop on Detecting Structure in Scholarly Discourse (DSSD), pp. 27-36.

For more information, see:

http://www.nactem.ac.uk/anatomy/

## File Format
IOB2 

| Column | Description        |
| ----- | ------------------ |
|id | a string feature. |
| start | begin character position |
| end chunk_tags| end character position|
|ner_tags| a list of classification labels|

## Labels

Anatomical_system
Cell
Cellular_component
Developing_anatomical_structure
Immaterial_anatomical_entity
Multi-tissue_structure
Organ
Organism_subdivision
Organism_substance
Pathological_formation
Tissue


## Example
<pre>
Ventricular	0	11	B-Multi-tissue_structure
fibrillation	12	24	O
</pre>