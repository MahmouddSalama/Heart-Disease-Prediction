import joblib 

def load_model(modelnum):
    if modelnum==0:
        return joblib.load('deploymet\logistic_regession')
    elif modelnum == 1:
        return joblib.load('deploymet\DecisionTreeClassifier')
    else:
        return joblib.load('deploymet\MultinomialNB')
    


def predict(l):
    c=load_model(0)
    return c.predict([l])[0]

