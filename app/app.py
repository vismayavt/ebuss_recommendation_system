from flask import Flask, request, jsonify
from model import get_user_recommendations

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask app is running!"

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    username = data.get("username", "")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    recommendations = get_user_recommendations(username)
    return jsonify({"recommendations": recommendations})

if __name__ == '__main__':
    app.run(debug=True)
