[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/) [![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=for-the-badge&logo=Jupyter)](https://jupyter.org/try)
# Hatch Hackathon `Domo Arigato Mr. Roboto`
Program for HATCH 2021 project of `Domo Arigato Mr. Roboto` Submitting Option 1 --> All code is on `VisualizingDataNEW.ipynb`
# Abstract
In this problem, there is a massive dataset provided to us where we have to create a model that will predict the level for a user's `history_class` between **strong_personal**, **strong_family**, **not_strong**, and **none**. There were many different criteria points that went into deciding this problem. I designed a sequential model under Keras which accurately detects the history class for any user. I also designed a **UI** for front-end user design (*still in development*).

# Data Control
The Datasheet has many different problems including **not having data for specific criteria**, **data is not formatted correctly**, **unequal distribution**, and **incorrect spelling** to name a few. As this is the type of dataset that one would have to deal with in the real world, it was a learning experience to work with this dataset. From over *2215* data points, I condensed it to *2171* points in order to have a general distribution of the data.

The following is an example of the **dataframe** of the data extracted as a result of `df.head()`. 
ID|Gene|History_class|Pathogenic|_method|cancer_dx|cancer_dx_age|cancer_dx_type|consent_approval|ethnicity|known_brca|known_cancer|other_cancer|rel_age|rel_cancer|rel_relation|relationships|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|0|No Gene|strong_personal|False|-|yes|57|pre-cancer vulvar due to hpv|yes|[caucasian]|unknown|yes|-|[70]|[leukemia, breast, ovarian, bladder, liver]|[mother, grandmother, grandfather, great aunt,...|-|
|1|No Gene|strong_personal|False|-|yes|57|pre-cancer vulvar due to hpv|yes|[caucasian]|unknown|yes|-|[70]|[leukemia, breast, ovarian, bladder, liver]|[mother, grandmother, grandfather, great aunt,...|-|

With further research and data analysis, I concluded that there were multiple data criteria that were unnecessary to the model which will just result in noise to the model, so I removed them from the data frame. (EX: `consent_approval`) 

When dealing with `rel_age`, `rel_cancer`, and `rel_relation` criteria points, I had to design such a program that will adapt to the different *check-box* format questions. For example for `rel_relation`, the user could select multiple different options out of a set of options. After generating a list of all possible options, I was able to control the type of data going through the model. (Example List Relationship: `['brother', 'sister', 'mother', 'father', 'aunt', 'uncle', 'grandfather', 'grandmother', 'great aunt', 'great uncle', 'great grandfather', 'great grandmother', 'cousin', 'niece', 'daughter']`) 

Relation of the data for 4 variables is shown 

![Image of the relation of data](https://github.com/Kunal2341/HatchHackathon/blob/main/readmeImgs/markdownRelationOfData.png?raw=true)


# Model Design
To begin, I used a keras model with taking in all the data points as in input layer, and then a couple of `Dense` and `dropout` layers. After multiple series of tests, I noticed that the results are lower than expected which resulted in an unnecessary amount of complexity.  (*Scroll down to see full model builds*)

I then used a Keras model, with a simpler set of `dense` and extra `sequential` layers resulting in a cleaner design of the model. I also used **adam** feature to optimize the model with the following $Adam Optimization - 1*10^3$ [*Github doesn't support latex*] formula. 

## Loss Graph
The image of loss graph is shown below
![Loss Graph](https://github.com/Kunal2341/HatchHackathon/blob/main/readmeImgs/markdownlossGraph1.png?raw=true)

## One-hot encoding design
When dealing with categorical variables under a sequential model, there needs to be a form of encoding the data into a numerical format. I used a one-hot encoding design that takes all possible types of data and formats the points in a `0` and `1` design resulting in either having that value or not. As per `ethnicity`, I had to condense the possible points to have a smaller data set. 

View below a described format of the dataset. 

![Image of Desibing Data](https://github.com/Kunal2341/HatchHackathon/blob/main/readmeImgs/markdownDescribeData.png?raw=true)

Before I used the following format to encode the categorical variable but it resulted in errors with the `model.fit()`

```python
def encode_string_categorical_feature(feature, name, dataset):
    index = StringLookup()
    feature_ds = dataset.map(lambda x, y: x[name])
    feature_ds = feature_ds.map(lambda x: tf.expand_dims(x, -1))
    index.adapt(feature_ds)
    encoded_feature = index(feature)
    encoder = CategoryEncoding(output_mode="binary")
    feature_ds = feature_ds.map(index)
    encoder.adapt(feature_ds)
    encoded_feature = encoder(encoded_feature)
    return encoded_feature
    
def encode_integer_categorical_feature(feature, name, dataset):
    encoder = CategoryEncoding(output_mode="binary")

    feature_ds = dataset.map(lambda x, y: x[name])
    feature_ds = feature_ds.map(lambda x: tf.expand_dims(x, -1))

    encoder.adapt(feature_ds)
    encoded_feature = encoder(feature)
    return encoded_feature
```

# Problems faced
There were a multifold set of problems I faced in all portions of the model, from desiging the model to trying to set up OCR for the document.
**Data Fitting** --> The format of the data was especially challenging to make sure everything was clean under the dataframe. I ran a lot of **explicit for-loops** resulting a much longer time to run the code making it inefficient, but as a matter of time, I wasn't able to implement **vectorization** to help speed up the process of formatting the data. On top of that, there were a lot of `.replace("","")` programs used to help clean up the data which is very manually done which could have better been implemented with **regex**
**Model** -->  When *fitting* and *training* the model I there were many errors with the **data type** including varying from `float`, `int64`, and `string` types using `df.dtypes()` as shown below. There were also challenged with formatting the input and output layers to match the data formats: `AssertionError: Could not compute output Tensor("Outputlayer/Sigmoid_20:0", shape=(None, 1), dtype=float32)` 
**OCR Document** --> I hoped to write a program where the user would upload the document and using OCR and location mapping on the document, extract the writing information from the **DomoArigatoSurvey** document. 

# Accuracy
At the current tests, it is running at a **72**% cumulative accuracy rate, but with the few data points after a **80** and **20** split there isn't much data to test on. 

## Run the program -- Front-end UI
I designed the UI for it to be run locally. Download the file name **streamlit.py** and run the following program in command line `streamlit run streamlit.py` after being in the same directory 
![Image of UI](https://github.com/Kunal2341/HatchHackathon/blob/main/readmeImgs/markdownUISurvery.png?raw=true)
<INSERT markdownUISurvery. png IMAGE>

## Run the program -- Install Libraries
Run the following program in your command line `pip install requirments.txt` which contains the following libraries
```
pandas==1.2.0
matplotlib==3.3.3
numpy==1.18.5
```

# Programmers Note
I am a junior in high school who has always been interested in AI and ML design. I am the founder and president of the AI club at my school and this hackathon has really opened my eyes to how much I really don't know about working with AI in the real world. Dealing with the uneven distribution of the data along with countless other problems was definitely a learning experience as it was my first time building a sequential model for these types of data. I was expanding my knowledge from the simpler (*in my point of view*) computer vision/OCR. 

# Possible future design changes
Run a better encoding format without explicit for-loops to help run the program faster while also running more efficient sequential model designs. 

# Model Design - 1
```python
Model: "functional_6"
__________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to                     
==================================================================================================
Pathogenic (InputLayer)         [(None, 11)]         0                                            
__________________________________________________________________________________________________
cancer_dx (InputLayer)          [(None, 1)]          0                                            
__________________________________________________________________________________________________
cancer_dx_age (InputLayer)      [(None, 1)]          0                                            
__________________________________________________________________________________________________
consent_approval (InputLayer)   [(None, 1)]          0                                            
__________________________________________________________________________________________________
known_brca (InputLayer)         [(None, 1)]          0                                            
__________________________________________________________________________________________________
known_cancer (InputLayer)       [(None, 1)]          0                                            
__________________________________________________________________________________________________
rel_age_1 (InputLayer)          [(None, 1)]          0                                            
__________________________________________________________________________________________________
rel_age_2 (InputLayer)          [(None, 1)]          0                                            
__________________________________________________________________________________________________
rel_age_3 (InputLayer)          [(None, 1)]          0                                            
__________________________________________________________________________________________________
category_encoding_35 (CategoryE (None, 2)            1           Pathogenic[0][0]                 
__________________________________________________________________________________________________
category_encoding_36 (CategoryE (None, 11)           1           cancer_dx[0][0]                  
__________________________________________________________________________________________________
category_encoding_37 (CategoryE (None, 74)           1           cancer_dx_age[0][0]              
__________________________________________________________________________________________________
category_encoding_38 (CategoryE (None, 11)           1           consent_approval[0][0]           
__________________________________________________________________________________________________
category_encoding_39 (CategoryE (None, 11)           1           known_brca[0][0]                 
__________________________________________________________________________________________________
category_encoding_40 (CategoryE (None, 11)           1           known_cancer[0][0]               
__________________________________________________________________________________________________
category_encoding_41 (CategoryE (None, 355664)       1           rel_age_1[0][0]                  
__________________________________________________________________________________________________
category_encoding_42 (CategoryE (None, 2012)         1           rel_age_2[0][0]                  
__________________________________________________________________________________________________
category_encoding_43 (CategoryE (None, 2083)         1           rel_age_3[0][0]                  
__________________________________________________________________________________________________
concatenate_3 (Concatenate)     (None, 359879)       0           category_encoding_35[0][0]       
                                                                 category_encoding_36[0][0]       
                                                                 category_encoding_37[0][0]       
                                                                 category_encoding_38[0][0]       
                                                                 category_encoding_39[0][0]       
                                                                 category_encoding_40[0][0]       
                                                                 category_encoding_41[0][0]       
                                                                 category_encoding_42[0][0]       
                                                                 category_encoding_43[0][0]       
__________________________________________________________________________________________________
Dense_1 (Dense)                 (None, 187)          67297560    concatenate_3[0][0]              
__________________________________________________________________________________________________
dropout_6 (Dropout)             (None, 187)          0           Dense_1[0][0]                    
__________________________________________________________________________________________________
Dense_2 (Dense)                 (None, 64)           12032       dropout_6[0][0]                  
__________________________________________________________________________________________________
dropout_7 (Dropout)             (None, 64)           0           Dense_2[0][0]                    
__________________________________________________________________________________________________
Dense_3 (Dense)                 (None, 32)           2080        dropout_7[0][0]                  
__________________________________________________________________________________________________
ethnicity (InputLayer)          [(None, 1)]          0                                            
__________________________________________________________________________________________________
rel_cancer (InputLayer)         [(None, 1)]          0                                            
__________________________________________________________________________________________________
rel_relation (InputLayer)       [(None, 1)]          0                                            
__________________________________________________________________________________________________
Outputlayer (Dense)             (None, 1)            33          Dense_3[0][0]                    
==================================================================================================
Total params: 67,311,714
Trainable params: 67,311,705
Non-trainable params: 9
__________________________________________________________________________________________________
```
# Model Design - 2
```python
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense (Dense)                (None, 8)                 648       
_________________________________________________________________
dense_1 (Dense)              (None, 4)                 36        
_________________________________________________________________
dense_2 (Dense)              (None, 1)                 5         
=================================================================
Total params: 689
Trainable params: 689
Non-trainable params: 0
_________________________________________________________________
```
