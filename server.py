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
    
    response = requests.get(apiUrl, params=params)
    if response.ok:
        data = response.json()
        print("Response JSON:", data)  # Added for deebug purposes
        if 'images' in data and data['images']:
            image_url = data['images'][0]['url']
            return jsonify({"message": image_url})
        else:
            return jsonify({"message": "No images found."})
    else:
        return jsonify({"message": "Request failed with status code: " + str(response.status)})

if __name__ == '__main__':
    app.run(debug=True)
