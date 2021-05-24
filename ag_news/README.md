# AG's News Topic Dataset - Classification
**Description**

AG (Antonio Gulli) 's News Topic Dataset is a collection of more than 1 million news articles. News articles have been gathered from more than 2000  news sources by ComeToMyHead in more than 1 year of activity. ComeToMyHead is an academic news search engine which has been running since July, 2004. The dataset is provided by the academic community for research purposes in data mining (clustering, classification, etc), information retrieval (ranking, search, etc), xml, data compression, data streaming, and any other non-commercial activity. 

* G. M. Del Corso, A. Gulli, and F. Romani. Ranking a stream of news. In Proceedings of 14th International World Wide Web Conference, pages 97–106, Chiba, Japan, 2005.  
  
* A. Gulli. The anatomy of a news search engine. In Proceedings of 14th International World Wide Web Conference, pages 880–881, Chiba, Japan, 2005.

The AG's news topic classification dataset is constructed by choosing 4 largest classes from the original corpus. Each class contains 30,000 training samples and 1,900 testing samples. The total number of training samples is 120,000 and testing 7,600.

The file classes.txt contains a list of classes corresponding to each label.
The files train.csv and test.csv contain all the training samples as comma-separated values.

**Entries**:  train 120,000  |	test 7,600   
**URL**: http://www.di.unipi.it/~gulli/AG_corpus_of_news_articles.html

## Format
| Column | Description        |
| ----- | ------------------ |
|class_id | a number from 1 to 4 - 1 represents World, 2 represents Sports, 3 represents Business and 4 represents Sci/Tech. |
|title| the news title|
|description | the news content |

### Example
<pre>
"3","Wall St. Bears Claw Back Into the Black (Reuters)","Reuters - Short-sellers, Wall Street's dwindling\band of ultra-cynics, are seeing green again."
"3","Carlyle Looks Toward Commercial Aerospace (Reuters)","Reuters - Private investment firm Carlyle Group,\which has a reputation for making well-timed and occasionally\controversial plays in the defense industry, has quietly placed\its bets on another part of the market."
</pre>






