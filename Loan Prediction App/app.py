import numpy as np
from flask import Flask,request,render_template
import pickle
import os

features=[]
gender=None
married=None
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    global features
    features.append(request.form.get("dependents"))
    features.append(request.form.get("applicantincome"))
    features.append(request.form.get("coapplicantincome"))
    features.append(request.form.get("loanamount"))
    features.append(request.form.get("loan_amount_term"))
    gender= request.form.get("gender")
    if gender==0:
        features.append(0)
        features.append(1)
    else:
        features.append(1)
        features.append(0)
    married=request.form.get("married")
    if married==1:
        features.append(0)
        features.append(1)
    else:
        features.append(1)
        features.append(0)
    education=request.form.get("education")
    if education==0:
        features.append(0)
        features.append(1)
    else:
        features.append(1)
        features.append(0)
    employed=request.form.get("self_employed")
    if employed==0:
        features.append(1)
        features.append(0)
    else:
        features.append(0)
        features.append(1)
    credit=request.form.get("credit_history")
    if credit==0:
        features.append(1)
        features.append(0)
    else:
        features.append(0)
        features.append(1)
    area = request.form.get("property_area")
    if area == 0:
        features.append(1)
        features.append(0)
        features.append(0)
    elif area==1:
        features.append(0)
        features.append(1)
        features.append(0)
    else:
        features.append(0)
        features.append(0)
        features.append(1)
    feature=np.array(features).reshape(1, -1)
    prediction=model.predict(feature)
    results=prediction[0]
    if results==0:
        result="Denied"
    else:
        result="Accepted"
    return render_template('index.html',output='Loan Application will be {}'.format(result))

print(len(features))

if __name__=="__main__":
    port=int(os.environ.get('PORT',5000))
    app.run(debug=True)