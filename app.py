from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
vec = pickle.load(open('vectorisation.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    
    tweet = request.form['message']
    
    prediction = model.predict(vec.transform([tweet]))
    return render_template('index.html', prediction=prediction)


if __name__ == "__main__":
    app.run(debug=True)
    