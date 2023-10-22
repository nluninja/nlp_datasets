# WNUT 17 Emerging Entities Dataset - Named Entity Extraction
## Description
he is the dataset for the WNUT 17 Emerging Entities task.  It contains text
from Twitter, Stack Overflow responses, YouTube comments, and Reddit comments.

This was downloaded from:

http://noisy-text.github.io/2017/emerging-rare-entities.html

Specifically, the following (train, dev, test) files:

http://noisy-text.github.io/2017/files/wnut17train.conll
http://noisy-text.github.io/2017/files/emerging.dev.conll
http://noisy-text.github.io/2017/files/emerging.test.annotated

The same data can also be downloaded from:

https://github.com/leondz/emerging_entities_17

(The files were identical.) For more information about this dataset, see:

http://noisy-text.github.io/2017/files/README.md


Leon Derczynski, Eric Nichols, Marieke van Erp, Nut Limsopatham (2017)
"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition",
in Proceedings of the 3rd Workshop on Noisy, User-generated Text

## Entries
train: 62730 entries  | test:  23394 entries | dev: 15733 entries


## URL / Attibution

Leon Derczynski, Eric Nichols, Marieke van Erp, Nut Limsopatham (2017)
"Results of the WNUT2017 Shared Task on Novel and Emerging Entity Recognition",
in Proceedings of the 3rd Workshop on Noisy, User-generated Text


## File Format
IOB2 

| Column | Description        |
| ----- | ------------------ |
|id | a string feature. |
|ner_tags| a list of classification labels|


| Labels |
| ------ |
| person
| location
| group
| corporation
| product
| creative-work


## Example
<pre>
From	O
Green	O
Newsfeed	O
:	O
AHFA	B-group
extends	O
deadline	O
</pre>