from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the models
decision_tree_model = pickle.load(open("models/decision_tree_regression_model.pkl", "rb"))
linear_regression_model = pickle.load(open("models/linear_regression_model.pkl", "rb"))
random_forest_model = pickle.load(open("models/random_forest_model.pkl", "rb"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    input_features = [np.array(features)]

    decision_tree_pred = decision_tree_model.predict(input_features)
    linear_regression_pred = linear_regression_model.predict(input_features)
    random_forest_pred = random_forest_model.predict(input_features)

    return jsonify({'decision_tree': decision_tree_pred[0],
                    'linear_regression': linear_regression_pred[0],
                    'random_forest': random_forest_pred[0]})

if __name__ == '__main__':
    app.run(debug=True)