#!flask/bin/python
from flask import Flask, request, jsonify
from flask import request
from sklearn.svm import SVC
from sklearn import datasets
import pickle

# load data
iris = datasets.load_iris()

# fit a model
svm = SVC(max_iter=10000)
svm.fit(iris.data, iris.target)

# save model
pickle.dump(svm, open('svm_model.pkl', 'wb'))

app = Flask(__name__)

@app.route('/is-alive')
def index():
    return "true"

@app.route('/predict', methods=['GET'])
def predict():
    sepal_length = float(request.args.get('sl'))
    sepal_width = float(request.args.get('sw'))
    petal_length = float(request.args.get('pl'))
    petal_width = float(request.args.get('pw'))
    loaded_svm = pickle.load(open('svm_model.pkl', 'rb'))
    prediction = loaded_svm.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    class_names = ['setosa', 'versicolor', 'virginica']
    response = {"species": class_names[prediction[0]]}
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=80,host='0.0.0.0')