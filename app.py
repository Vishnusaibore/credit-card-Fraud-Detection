from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('smote_model.pkl','rb'))

@app.route('/')
def hello_world():
    return render_template("fraud.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    print(int_features)
    prediction=model.predict(final)
    

    if prediction==1:
        return render_template('fraud.html',pred='The Transaction is Fraud')
    else:
        return render_template('fraud.html',pred='The Transaction is Not a Fraud')


if __name__ == '__main__':
    app.run(debug=True)