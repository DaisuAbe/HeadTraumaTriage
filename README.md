# HeadTraumaTriage
A prehospital triage system to detect traumatic intracranial hemorrhage using machine learning algorithms

This is a repository in which anyone can use our prediction model to detect traumatic intracranial hemorrhage in head trauma patients.

Description to use this repository.
1. If you are going to use the all-elements model, you need to over-write the "demo-data_for_all-elements_model" with your data, and implement "All-elements_model.py". You will get the probabilities of each data and you will also get the 1 or 0 result judged from the cut-off value which we set in our article.
2. If you will try the five-elements model, you need to choose the "demo-data_for_five-elements_model" and edit it in a same way above, and implement "Fve-elements_model.py" to get the prediction results.

Input for each feature
sex; 1:male, 0:female
Age[years old], E-GCS, Body temperature[°C], Heart rate[beat per minute], Respiratory rate[per minute], Sytolic blood pressure[mmHg]: discrete quantity 
Alcohol intake,	Polytrauma,	High-energy head trauma,	Pupil abnormality,	Head trauma scar,	Hemiplegia,	Vomiting,	Loss of consciousness,	Seizur,e	Talk and deteriorate,	Disorientation; positive:, negative:0
