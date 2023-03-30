import joblib 

def load_model(modelnum):
    if modelnum==0:
        return joblib.load('deploymet\logistic_regession')
    elif modelnum == 1:
        return joblib.load('deploymet\DecisionTreeClassifier')
    else:
        return joblib.load('deploymet\MultinomialNB')
    


def predict(modelnum,male,age,BPMeds,prevalentHyp,diabetes,totChol,sysBP,diaBP,BMI,glucose):
    c=load_model(modelnum)
    return c.predict(([[male,age,BPMeds,prevalentHyp,diabetes,totChol,sysBP,diaBP,BMI,glucose]]))[0]

