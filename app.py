#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


data = pd.read_csv('tsdata.csv')


# In[5]:


data.drop('Unnamed: 0',axis=1,inplace=True)


# In[7]:


x=data.iloc[:,0:-1]
y=data.iloc[:,-1]


# In[8]:


from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest = train_test_split(x,y,test_size=0.25)


# In[9]:


from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()


# In[10]:


model.fit(xtrain,ytrain)


# In[ ]:


from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/')

def xyz():
    return render_template('tss.html')
@app.route('/tensile', methods=['GET','POST'])

def abc():
    if(request.method=='POST'):
        norm_temp=float(request.form['not'])
        temp_temp=int(request.form['tet'])
        sili=float(request.form['sip'])
        chrom=float(request.form['chp'])
        copp=float(request.form['cop'])
        nick=float(request.form['nip'])
        sulp=float(request.form['sup'])
        carb=float(request.form['cap'])
        mang=float(request.form['map'])
        result=model.predict([[norm_temp,temp_temp,sili,chrom,copp,nick,sulp,carb,mang]])
        return render_template('tss.html',answer=result)
if __name__=='__main__':
    app.run()

