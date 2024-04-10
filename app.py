from flask import Flask, request, jsonify, render_template
from topk import topKFrequent

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/topk', methods=['POST'])
def topk():
    data = request.form
    nums = [int(num.strip()) for num in data['nums'].split(',')]
    k = int(data['k'])
    result = topKFrequent(nums, k)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)


