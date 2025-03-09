1. titanic_capstone contains the various models and their accuracy. It also uses joblib to serialize model object.
2. The dataset can be found here: https://www.kaggle.com/c/titanic/data
3. titanic_model.pkl contains the serliazed model object. titanic_model.pkl will be used for model deployment.
4. app.py contains code based on Flask to interact with the model. Use postman to post json request, sample request is provided in sample_postman_json
5. requirements.txt contains the list of dependencies required to run the model (pip freeze > requirements. txt).
6. Dockerfile to build container image for the model.
7. The image can also be found at this public repo: ksaurabh/mlops-demo
