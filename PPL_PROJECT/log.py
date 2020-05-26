
import speech_recognition as sr
import pandas as pd
import sys
import os
from gtts import gTTS

    
#voice input for region
a = {'Bengaluru':1, 'Bhubhaneshwar':2, 'Chennai':3, 'Chandigarh':4, 'Delhi':5}
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    s1 = "Please mention the region to which you belong"
    tts1 = gTTS(s1)
    tts1.save('intro.mp3')
    os.system('mpg123 intro.mp3')
    audio = r.listen(source)
    print("Recognizing Now ... ")
try:
    dest = r.recognize_google(audio)
    if dest!='Bengaluru' and dest!='Bhubhaneshwar' and dest!='Chennai' and dest!='Chandigarh' and dest!='Delhi':
        a[dest] = 6
        print("Updated dictionary is:", a) 
    print(dest)
except Exception as e:
    print("Error : " + str(e))
    print("Could not recognize properly.Please try again!")
    sys.exit() 
 
#voice input for age	
s = sr.Recognizer()
with sr.Microphone() as source:
    s.adjust_for_ambient_noise(source)
    s2 = "Please mention the age"
    tts2 = gTTS(s2)
    tts2.save('intro2.mp3')
    os.system('mpg123 intro2.mp3')
    audio = s.listen(source)
    print("Recognizing Now ... ")
try:
    age = s.recognize_google(audio)  
    print(age)
except Exception as e:
    print("Error : " + str(e))
    print("Could not recognize properly.Please try again!")
    sys.exit() 
 
 
#voice input for Coma score
f = sr.Recognizer()
with sr.Microphone() as source:
    f.adjust_for_ambient_noise(source)
    s3 = "Please mention the coma score"
    tts3 = gTTS(s3,lang = 'en')
    tts3.save('intro3.mp3')
    os.system('mpg123 intro3.mp3')    
    audio = f.listen(source)
    print("Recognizing Now ... ")
try:
    score = f.recognize_google(audio) 
    print(score)   	
except Exception as e:
    print("Error : " + str(e))
    print("Could not recognize properly.Please try again!")
    sys.exit() 
 

#voice input for Charlson Index
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    s4 = "Please mention the Charlson index"
    tts4 = gTTS(s4,lang = 'en')
    tts4.save('intro4.mp3')
    os.system('mpg123 intro4.mp3')    
    audio = r.listen(source)
    print("Recognizing Now ... ")
try:
    index = r.recognize_google(audio) 
    print(index)   	
except Exception as e:
    print("Error : " + str(e))
    print("Could not recognize properly.Please try again!")
    sys.exit() 

t = a[dest]
col_names = ['Region','Age','Coma score','HBB','Charlson Index','Blood Glucose','Infect_Prob','label']# columns in the dataset
data = pd.read_csv("train2.csv",header=None, names=col_names)
data.head()
feature_cols = ['Region','Age','Coma score','Charlson Index']#required columns 
X = data[feature_cols] 
y = data.label
#print(data.info()) just to print the info of the data


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)#splitting the dataset into train and test


from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train,y_train)#fit the model


y_pred = logreg.predict(X_test) #predict

from sklearn import metrics

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("Precision:",metrics.precision_score(y_test, y_pred))
print("Recall:",metrics.recall_score(y_test, y_pred))


xnew = [[t,int(age),int(score),int(index)]]#predict for a new example
ynew = logreg.predict_proba(xnew)
print("X=%s, Predicted=%s" % (xnew[0], ynew[0]))

#ynew is an array first element represents the probability that person will not get covid19 infection
#and 2nd element says probability he may have an infection


