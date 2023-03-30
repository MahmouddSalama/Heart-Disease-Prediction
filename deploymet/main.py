from msilib.schema import TextStyle
import tkinter as tk
from tkinter import *
from tkinter import ttk
from turtle import position, width
from help import predict

def task(modelnum,male,age,BPMeds,prevalentHyp,diabetes,totChol,sysBP,diaBP,BMI,glucose):
    d={
        0:'No',
        1:'Yes'
    }
    res=predict(modelnum,male,age,BPMeds,prevalentHyp,diabetes,totChol,sysBP,diaBP,BMI,glucose)
    #res =predict(1,1,39,0.0,0,0,195.0,106.0,70.0,26.97,77.0)
    tk.Label(root, text="The prediction value for heart stock is {}".format(d[res])).place(x=220, y=255)

# setting root window:
root = tk.Tk()
root.title("heart Stroke Prediction")
root.geometry("600x280")
###############################################################################
options = ["Logistic Regression", "DecisionTreeClassifier", "MultinomialNB"]
models={

    "Logistic Regression":0,
    "DecisionTreeClassifier":1,
    "MultinomialNB":2,
}
##############################################################################################################################################################################3
tk.Label(root, text="male").place(x=50, y=35)
male=Entry(root)
male.place(x=150,y=35)
###################################
tk.Label(root, text="age").place(x=50, y=60)
age=Entry(root)
age.place(x=150,y=60)
#####################################
tk.Label(root, text="BPMeds").place(x=50, y=85)
BPMeds=Entry(root)
BPMeds.place(x=150,y=85)
#####################################
tk.Label(root, text="prevalentHyp").place(x=300, y=35)
prevalentHyp=Entry(root)
prevalentHyp.place(x=420,y=35)
#####################################
tk.Label(root, text="diabetes").place(x=300, y=60)
diabetes=Entry(root)
diabetes.place(x=420,y=60)
# ##########################################
tk.Label(root, text="totChol").place(x=300, y=85)
totChol=Entry(root)
totChol.place(x=420,y=85)
#####################################
tk.Label(root, text="sysBP").place(x=300, y=110)
sysBP=Entry(root)
sysBP.place(x=420,y=110)
#####################################
tk.Label(root, text="diaBP").place(x=300, y=135)
diaBP=Entry(root)
diaBP.place(x=420,y=135)
# ##########################################
tk.Label(root, text="BMI").place(x=300, y=160)
BMI=Entry(root)
BMI.place(x=420,y=160)
###################################
tk.Label(root, text="glucose").place(x=50, y=110)
glucose=Entry(root)
glucose.place(x=150,y=110)
###################################
tk.Label(root, text="Model number").place(x=50, y=135)
model=Entry(root)
model.place(x=150,y=135)
#####################################

selected_option = tk.StringVar()

# set the initial value of the StringVar
selected_option.set(options[0])

# create the OptionMenu widget
option_menu = tk.OptionMenu(root, selected_option, *options,)
option_menu.place(x=150,y=150)
option_menu.pack()
print(selected_option)

####################################

b=Button(root,text="predict",width=15,command=lambda:task(
models[selected_option.get()],
float('0'+male.get()),
float('0'+age.get()),
float('0'+BPMeds.get()),
float('0'+prevalentHyp.get()),
float('0'+diabetes.get()),
float('0'+totChol.get()),
float('0'+sysBP.get()),
float('0'+diaBP.get()),
float('0'+BMI.get()),
float('0'+glucose.get()),
))

b.pack()
b.place(x=250,y=220)

############################################
# window in mainloop:

root.mainloop()
