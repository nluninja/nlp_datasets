# Toxic Comments Classification Dataset - Classification
## Description

The Toxic Comments Classification Dataset consists of a large number of Wikipedia comments which have been labeled by human raters for toxic behavior.   

The dataset has been provided by the Conversation AI team, a research initiative founded by Jigsaw and Google (both a part of Alphabet) that are working on tools to help improve online conversation. One area of focus is the study of negative online behaviors, like toxic comments (i.e. comments that are rude, disrespectful or otherwise likely to make someone leave a discussion). 

The dataset has been published as part of a Kaggle Challenge, which asked data scientists to build a multi-headed model that’s capable of detecting different types of of toxicity like threats, obscenity, insults, and identity-based hate better than AI Team’s current models.

## Entries
train xx  |	test xx  

## URL 
https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data

## Data Format
text - csv  

| Column | Description        |
| ----- | ------------------ |
|comment_text| text content|
|id| text content identifier|
|identity_hate|a score value for identity_hate|
|insult|a score value for insult|
|obscene|a score value for obscene|
|severe_toxic|a score value for severe_toxic|
|threat|a score value for threat|
|toxic| a score value for toxic|
|toxicity| a score for toxicity|
|set| the train/test set|

## Example
<pre>
comment_text,id,identity_hate,insult,obscene,set,severe_toxic,threat,toxic,toxicity
explanation why the edits made under my username hardcore metallica fan were reverted  they weren t vandalisms  just closure on some gas after i voted at new york dolls fac  and please don t remove the template from the talk page since i m retired now ,0000997932d777bf,0.0,0.0,0.0,train,0.0,0.0,0.0,0.0
you  sir  are my hero  any chance you remember what page that s on ,0001d958c54c6e35,0.0,0.0,0.0,train,0.0,0.0,0.0,0.0
</pre>





