
# Simplifier - INTELLIGENT QUESTION PAIR ANALYSIS USING DEEP LEARNING

Today, the world is driven by data and many new technologies and products are at the forefront to provide the right information to users instantly. Every day, we search for thousands of queries related to each domain and that too, in an entirely different way. Based on regions and other factors, the pattern of question changes (semantics) but may have the exact same meaning. This brings a challenge to store answers for every such pattern within the server in order to provide the right answer. So our idea is to analyze two questions and extract certain parameters to determine the similarity of those questions. The deep learning technology is used in the project to find the similarity. Instead of checking for statement similarity, it analyses the sentence intelligently to identify accurately, the meaning of the questions and to output the similarity. Thus by identifying the similarity, it is very useful in many domains that enable them to store only a single copy of the answer for multiple questions having the same meaning. It can also be employed in chatbots and automated answer evaluation software where faculty can check the similarity of answers written by students to the exact answer, thus given marks accordingly. There emerge more domains where this project has a significant role in eliminating redundancy and making daily life more progressive.
## Modules
(1) Query Input Module \
(2) Pre-processing Module \
(3) Feature Engineering Module \
(4) Training Module\
(5) Testing Module\
(6) Output Generation Module

## Dataset

  [Quora Question Pair Dataset](https://www.kaggle.com/c/quora-question-pairs/data)

## Model
Our model is the most efficient and the most effective for question similarity calculation.
We fuse both CNN and BiLSTM to get accurate and precise output. In our model three
inputs, we have question 1, question 2, and feature engineering values of two questions.
The two input questions are passed to the embedding layer and copy the output into three.
The two copies are passed into the Conv1D layer and one copy is passed to BiLSTM.
The output of the two Conv1D layers is passed into the GlobalMaxPool layer to reduce
the dimension into two and then concatenate both. At the same time, the output of
BiLSTM and dense output of feature engineering are concatenated. Then the output of
both layers is separately passed to the BatchNormalization layer, then to the Dropout
layer, and followed by that, to the Dense layer. Now we concatenate both of them and
then passed to series of different layers and finally predict the output using a sigmoid
function.

|Data|Accuracy|Log-loss|
|:--------:|:--------:|:--------|
|Train Data| 89% | 0.22|
|Validation Data | 89%| 0.23|

 


![model_plot (2)](https://user-images.githubusercontent.com/45265641/125159284-23fb1900-e194-11eb-9a11-a1bc408cbddf.png)

## Screenshots of working model

![homepage_1](https://user-images.githubusercontent.com/45265641/125160785-73ddde00-e19c-11eb-8132-35319c3d0bfc.png)
![homepage_2](https://user-images.githubusercontent.com/45265641/125160786-750f0b00-e19c-11eb-9f84-c3137db07d1c.png)
![homepage_3](https://user-images.githubusercontent.com/45265641/125160788-75a7a180-e19c-11eb-864b-72444994a5b3.png)
![homepage_4](https://user-images.githubusercontent.com/45265641/125160789-75a7a180-e19c-11eb-97f9-4257c1c7137d.png)

## To run the progrom
1. Install requirment.txt
2. Extract venv.rar
3. Extract q_dict.rar
4. Extract model.part1.rar 
5. Create glove_model.pickle by running the below code seperatly
```python  
import pickle
import gensim

!wget http://nlp.stanford.edu/data/glove.840B.300d.zip
!unzip glove.840B.300d.zip

from gensim.scripts.glove2word2vec import glove2word2vec
glove2word2vec(glove_input_file="glove.840B.300d.txt", word2vec_output_file="glove_vectors.txt")

from gensim.models.keyedvectors import KeyedVectors
glove_model = KeyedVectors.load_word2vec_format("glove_vectors.txt", binary=False)

with open('glove_model.pickle','wb') as handle:
  pickle.dump(glove_model,handle,protocol= pickle.HIGHEST_PROTOCOL )
  ```
 6. Open the Simplifier folder in any IDLE
 7. Run process.py 
