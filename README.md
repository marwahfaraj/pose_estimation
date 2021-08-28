# Pose estimation applications
![](image/1.jpg)
----
## Marwah Faraj<br>

[Linkedin](https://www.linkedin.com/in/marwah-faraj) | [Github](https://github.com/marwahfaraj) | [E-mail](marwah.faraj777@gmail.com) |
[Arabic tweets Dataset](https://www.kaggle.com/imranzaman5202/arabic-twitter-sentiment-analysis) |
[Poject Presentation](https://docs.google.com/presentation/d/1d0JpkFl4v2SmU5rNBB0BBUtDjkcjWBKW0OpI3TrwZPw/edit#slide=id.ge29597d775_0_1)
----
# Table of Contents
1. [Background and Motivation](#background-and-motivation)
2. [Data](#data)  
    - [Description](#description)
    - [Pipline](#pipline)  
   
5. [Exploration](#exploration)
6. [Visualization](#visualization)
7. [Machine Learning](#ml)
8. [Conclusions](#conclusions)
9. [Further Study](#further-study)

## Background and Motivation
Implementing sentiment analysis in Arabic Language. I’m using NLP (Natural Language Processing) to demonstrate that and Machine Learning Algorithms to classify whether the sentiment is positive or negative.

----
## Data
This dataset consists of more than 56 thousand tweets in Arabic Language, and it is devided into 2 part, more than 28500 positive tweets and more than 28300 negative tweet, and it does not contain any null value.



## Description
# Arabic Script
- Written right-to-left<br>
- Letters have contextual variants<br>
- Used to write many languages besides Arabic: Persian, Kurdish, Urdu, etc.<br>

![](image/arabic.png)

# The main challenges for Arabic Language Processing:
- Orthographic ambiguity                         الابهام  الاملائي<br>
- Morphological richness                           الغنى الصرفي<br>
- Dialectal variation                              تعدد اللهجات
- Orthographic inconsistency                     الاخطاء الاملائية
- Resource poverty (data & tools)    فقر موارد البيانات والادوات
- Limited research                         البحث العلمي المحدود


----
## Pipline
The pandas, numpy, NLTK library, machine learning: Multinomial Naive Bayes, Gaussian Naive Bayes, Ridge_classifier, Logstic Regression, Random Forest, deep learning: Multilayer perseptron/ Tenseorflow, keras,  matplotlib, and seaborn software libraries was used to examine, plot, analyze and classify this data.<br>

----
## Exploration
Noticed this dataset do not contian null values as shown in the dataset info, but noticed that it contains a lot of emojies. 
After further exploration notice that there is english words and english numbers in the dataset, and the dataset is a balance data.

# visualization
## The data status: Balance data

![](image/balance_data.jpg)

The arabic people use the word ‘God’ a lot in their conversation and as shown the most common word is ‘God’

![](image/postive_top_words.jpg)

For the same reason the most common word in the negative tweets is ‘God’

![](image/negative_top_words.jpg)

----
## Machine Learning
Diffrient machine learning algorithms implemented and used to predict on unseed dataset to classify new tweet and give diffrint scores as detailed below:<br>
1- Naive Bayes Algorithm:
- Multinomial Naive Bayes Algorthim: <br>
  Accuracy= 0.767<br>
  Precision= 0.770<br>
  Recall= 0.760<br>
  F1= 0.770<br>
- Gaussian Naive Bayes Algorthim: <br>
  Accuracy= 0.741<br>
  Precision= 0.830<br>
  Recall= 0.610<br>
  F1= 0.700<br>
  
 2- Ridge Classifier:<br>
   Accuracy= 0.792<br>
   Precision= 0.810<br>
   Recall= 0.770<br>
   F1= 0.790<br>
   
 3- LogisticRegression Algorithm:<br>
    Accuracy= 0.790<br>
    Precision= 0.820<br>
    Recall= 0.750<br>
    F1= 0.780<br>
    
 4- Random Foreset Algorthim:<br>
     Accuracy= 0.677<br>
     Precision= 0.780<br>
     Recall= 0.490<br>
     F1= 0.600<br>
     
  ## Deep Learning
  1- Multi layer perseptron:<br>
    loos score= 0.4372<br>
    Accuracy= 0.804<br>
   
   ![](image/mlp_cm.jpg)
   
 The MLP model did not predict all the positive and negative tweets correctly, as it appeared in the graph, there are 974 negative tweet were predicted positive, also there are 1251 positive tweets were predicted negative.  
 
 ## Machine Learning Algorithms comparison:
 
 ![](image/model_comparision.jpg)
 
 Nural Newtwork/ Multi layer perceptrone gave the higher accuracy score 80.4% but it is a time consuming to train, and for that Ridge classifier model took less time to train and gave a 79.2%.
 The MLP model is deployed in flask app to predict on new tweet and classify it weather it is positive or negative.

----
## Conclusions
- Using deep learning by applying Multilayer Perceptron (MLP) in prediction gave the higher accuracy among the models 80.4%.<br>
- Sentiment analysis is extremely useful in social media monitoring as it allows us to gain an overview of the wider public opinion behind certain topics, and monitor for toxic posts to warn and ban offending users.

  
----
## Further study
- Consider emoji and how it could change the analysis.
- Use Camel Tool Modules in preparing the text to use in machine learning Models. (Arabic Language specific library)

![](image/n_wordcloud.jpg)
