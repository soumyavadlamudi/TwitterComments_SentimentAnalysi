# Identify-the-Sentiments
Twitter data sentiment Analysis
The contest URL: https://datahack.analyticsvidhya.com/contest/linguipedia-codefest-natural-language-processing-1/

## About Problem: Identify the Sentiments
Sentiment analysis is contextual mining of text which identifies and extracts subjective information in source material, and helping a business to understand the social sentiment of their brand, product or service while monitoring online conversations. Brands can use this data to measure the success of their products in an objective manner. In this challenge, you are provided with tweet data to predict sentiment on electronic products of netizens.

### DS Resources :-
- Get started with NLP and text classification with our latest offering  ‘Natural Language Processing (NLP) using Python’ course
- Refer this comprehensive guide that exhaustively covers text classification techniques using different libraries and its implementation in python.
- You can also refer this guide that covers multiple techniques including TF-IDF, Word2Vec etc. to tackle problems related to Sentiment Analysis.

### Problem Statement
Sentiment analysis remains one of the key problems that has seen extensive application of natural language processing. This time around, given the tweets from customers about various tech firms who manufacture and sell mobiles, computers, laptops, etc, the task is to identify if the tweets have a negative sentiment towards such companies or products.

### Dataset
The train set contains 7,920 tweets The test set contains 1,953 tweets

### Data Pre-processing
(It's pretty standard so I took it from here - Link)


Lower-case all characters
Remove twitter handles
Remove urls
Replace unidecode characters
remove @, emails
Only keep characters
Keep words with length>1 only
Replace words like 'whatisthis' to ' what is this'
Remove repeated spaces
Replace '@[^\s]' with 'vulgar'

### Evaluation Metric
The metric used for evaluating the performance of classification model would be weighted F1-Score.

### Acknowledgement
Many snippets of the code used may have been taken from other open GitHub repositories to ease the rapid production and pace up the flow in the competition. I am thankful to all of them for their mentorship and help.


**Note :-** Most profane and vulgar terms in the tweets have been replaced with “$&@*#”. However, please note that the dataset still might contain text that may be considered profane, vulgar, or offensive.
