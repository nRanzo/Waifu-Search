from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['GET'])
def chat():
    user_input = request.args.get('input')
    apiUrl = 'https://api.waifu.im/search'
    params = {
        'included_tags': [user_input],
        'height': '>=2000'
    }
    queryParams = {}
    for key, value in params.items():
        if isinstance(value, list):
            for v in value:
                if key in queryParams:
                    queryParams[key].append(v)
                else:
                    queryParams[key] = [v]
        else:
            queryParams[key] = value

    response = requests.get(apiUrl, params=queryParams)
    if response.ok:
        data = response.json()
        return jsonify({"message": data})
    else:
        return jsonify({"message": "Request failed with status code: " + str(response.status)})

if __name__ == '__main__':
    app.run(debug=True)
