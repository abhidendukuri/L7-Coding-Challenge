import plotly
import plotly.graph_objects as go
import math
import re
import json
from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import secure_filename

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['txt', 'csv'])

@app.route('/')
def home():
    return render_template('upload.html')

@app.route('/censusdata', methods=['POST', 'GET'])
def upload():
    
    leadDigits = dict()
    count = 0
    f = request.files['file']

    fin = open(f.filename)
    for line in fin:
        # Find the numbers in each line 
        # since the findall returns a list, we'll pop the element to extract a string
        n = re.findall(r'\d+', line).pop()
        
        # equation to find the lead digit of each value
        lead = int(n) // 10 ** (len(n) - 1)

        # add each lead digit to dictionary
        if lead in leadDigits:
            leadDigits[lead] += 1
        else:
            leadDigits[lead] = 1

        # get the total values count
        count += 1

    fin.close()
    
    bar = plot(leadDigits, count)
    
    return render_template("index.html", plot = bar)

def plot(leadDigits, count):

    # Create the arrays to plot
    # the x-axis
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    # the y-axes
    benford = []
    inp = []

    for i in range(1, 10):
        benford.append(math.log10((i + 1) / i))
    
    for key in sorted(leadDigits.keys()):
        inp.append( leadDigits[key] / count)


    data = [
        go.Bar(name = "Benford's Law", x = nums, y = benford),
        go.Bar(name = "Census Data", x = nums, y = inp)
    ]

    graphJSON = json.dumps(data, cls = plotly.utils.PlotlyJSONEncoder)

    return graphJSON

    
if __name__ == "__main__":
    app.run(debug = True, host = '0.0.0.0')