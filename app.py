from flask import Flask, render_template, jsonify
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/')
def home():

    try:
        with open('instance/data/data.json', 'r') as file:
            data = json.load(file)
            current_year = datetime.now().year
            return render_template('index.html', data=data, year=current_year)

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
