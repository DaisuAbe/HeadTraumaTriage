# HeadTraumaTriage
## Introduction
This is a repository in which anyone can use our prediction models to detect traumatic intracranial hemorrhage in head trauma patients.

## Setup
We run the code below on Python 3.6 with the packages listed in requiements.txt.

## How to use
If you are going to use the all-elements model, you need to overwrite the "demo-data_for_all-elements_model" with your data and implement "All-elements_model.py". You will obtain the probability of your data, and you will also obtain the 1 or 0 result judged from the cutoff value that we set in our article.

If you will try the five-elements model, you need to choose the "demo-data_for_five-elements_model" and edit it in the same way above and implement "Five-elements_model.py" to get the prediction results.

Input for each feature 
sex; 1:male, 0:female, Age[years old], E-GCS, Body temperature[°C], Heart rate[beat per minute], Respiratory rate[per minute], Sytolic blood pressure[mmHg]: discrete quantity Alcohol intake, Polytrauma, High-energy head trauma, Pupil abnormality, Head trauma scar, Hemiplegia, Vomiting, Loss of consciousness, Seizure ,Talk and deteriorate, Disorientation; positive:, negative:0
