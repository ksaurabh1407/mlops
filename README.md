1. titanic_capstone contains the various models and their accuracy. It also uses joblib to serialize model object.
2. titanic_model.pkl contains the serliazed model object. titanic_model.pkl will be used for model deployment.
3. app.py contains code based on Flask to interact with the model.
4. requirements.txt contains the list of dependencies required to run the model (pip freeze > requirements. txt).
5. Dockerfile to build container image for the model.
6. The image can also be found at this public repo: ksaurabh/mlops-demo
