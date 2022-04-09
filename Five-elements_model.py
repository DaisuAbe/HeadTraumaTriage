#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import pickle

# Load the five-elements model
filename = 'five-elements_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))

# Load the demo data
X_data = pd.read_csv('demo-data_for_five-elements_model.csv')

# Make predictions and output the probability of the case
y_predicted = loaded_model.predict_proba(X_data)[:, 1]
probability = y_predicted * 100
print("Probability:", probability)

# Set a cut-off value and 
# In this demo, we set 10.392025 as the cut-off value, because we adopted this value in our article.

for i in probability:
    if i >= 10.392025:
        result=1
    else:
        result=0
print("Prediction result:", result)


# In[ ]:





# In[ ]:




