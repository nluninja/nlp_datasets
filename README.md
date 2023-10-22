# A not-complete list of datasets for NLP tasks

A useful list of datasets I collected for NLP tasks. You can fork and/or clone this repository and get all the datasets available.

```bash
git clone https://github.com/nluninja/nlp_datasets
```


## Available datasets

| Name | Description | classes | format | language |
| ---- | ----------- | ------- | ------ | -------- |
| [`20 Newsgroups dataset`](./20_newsgroup/) | file set arranged into 20 topic folders | see corpus page | files | en  |
| [`AG News Topic dataset`](./ag_news/) | News Topic Classification dataset - Antonio Gulli -  UniPi | World, Sports, Business, Sci/Tech | csv | en  |
| [`CoNLL 2003`](./conll2003/) | named entity recognition dataset | People, Location, Organization, Misc | conll/iob2 | en  |
| [`emotions classification dataset`](./emotion_classification_dataset/) | emotion classification dataset which contains tweets labeled into 6 categories | joy, sadness, anger, fear, love, surprise | csv | en |
| [`Georgetown University Multilayer corpus in CoNLL`](./GUM/) | CoNLL tagged corpus for entity extraction| 23 classes (person, substance, quantity, time, place, organization) | conll/iob2 | en  |
| [`Relationship and Entity Extraction Evaluation Dataset in CoNLL`](./re3d/) | CoNLL tagged corpus for entity extraction| 21 classes (person, temporal, weapon, MilitaryPlatform, quantity, organization) | conll/iob2 | en  |
| [`sentiment140 dataset`](./sentiment140_dataset/) | dataset which contains tweets labeled according to their polarity |negative, neutral, positive | csv | en |
| [`Toxic Comments dataset Reviews`](./toxic_comments/) | Wikipedia comments labeled into 6 categories with score | toxic, severe_toxic, obscene, threat, insult, identity_hate| csv | en  |
| [`WikiGold Dataset`](./wikigold/) | named entity recognition dataset | People, Location, Organization, Misc | conll/iob2 | en  |
| [`Wikipedia Movie Plots dataset`](./wikipedia_movie_plots/) | descriptions of movies from around the world scraped from WikiPedia | Genre Classes | csv | en  |
| [`WNUT 17 Emerging Entities Dataset`](./WNUT17/) | Twitter/StackOverflow data for discovering emerging entities | Entity Classes | conll/iob2 | en  |
| [`Yelp! Reviews`](./yelp_reviews/) | reviews dataset from Yelp! for classification/sentiment analysis tasks| 1 to 5 rates | csv | en  |


I appreciate your contribution to this repo, so don't hesitate to submit your changes via pull request for bug fixing or for adding a new dataset as well! 

```bash
pull request https://github.com/nluninja/nlp_datasets
```

use the [corpus_template](./corpus_template) for uploading the new dataset. I look forward seeing your contribution! :pray: :kissing_heart: 