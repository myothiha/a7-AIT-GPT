from flask import Flask, render_template, request
import numpy as np
import cloudpickle

app = Flask(__name__)

with open('models/chatbots.pkl', 'rb') as f:
    model = cloudpickle.load(f)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/answer', methods=['POST'])
def generate_jokes():

    question = request.form.get('question')
    answer = model({"question": question})

    return render_template('index.html', question = question, answer = answer)


port_number = 8000

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port_number)