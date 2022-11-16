# Italian NLP Corpus - Classification/Sentiment Analysis
## Description

__Corpus of Sentences rated with Human Complexity Judgments__

This corpus contains 1,123 Italian sentences and 1,200 English sentences rated by humans with a judgment of complexity. Judgments were collected through a crowdsourcing task in which 20 native speakers of each language were asked to judge how difficult they perceived a given sentence on a complexity scale from 1 (i.e. “very easy”) to 7 (i.e. “very difficult”). 

The datasets of sentences used for the task were taken from two different manually revised treebanks: the newspaper section of the Italian Universal Dependency Treebank (IUDT) for the Italian experiment, and the automatically converted Wall Street Journal section of the Penn Treebank for the English experiment."


___Brunato D., De Mattei L., Dell’Orletta F., Iavarone B., Venturi G. (2018) “Is this Sentence Difficult? Do you Agree?“. In Proceedings of the 2018 Conference on Empirical Methods in Natural Language Processing (EMNLP 2018), 31–4 November, Bruxelles.__


## Entries

 train: 
 * Italian 1,123 sentences
 * English 1,200 sentences


## URL
http://www.italianlp.it/

## Format
text - csv  

| Column | Description        |
| ----- | ------------------ |
|class_index | a number from 1 to 5 |
|review | the text of the review |

## Example
<pre>
"5","dr. goldberg offers everything i look for in a general practitioner.  he's nice and easy to talk to without being patronizing; he's always on time in seeing his patients; he's affiliated with a top-notch hospital (nyu) which my parents have explained to me is very important in case something happens and you need surgery; and you can get referrals to see specialists without having to see him first.  really, what more do you need?  i'm sitting here trying to think of any complaints i have about him, but i'm really drawing a blank."
"2","Unfortunately, the frustration of being Dr. Goldberg's patient is a repeat of the experience I've had with so many other doctors in NYC -- good doctor, terrible staff.  It seems that his staff simply never answers the phone.  It usually takes 2 hours of repeated calling to get an answer.  Who has time for that or wants to deal with it?  I have run into this problem with many other doctors and I just don't get it.  You have office workers, you have patients with medical needs, why isn't anyone answering the phone?  It's incomprehensible and not work the aggravation.  It's with regret that I feel that I have to give Dr. Goldberg 2 stars."
</pre>


