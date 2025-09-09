from flask import Flask, jsonify, request
import os

app = Flask(__name__)

# Placeholder for Cosmic Grain logic
# In a real scenario, this would interact with your numeric paradigm.
# For the hackathon, we simulate a response.
def get_cosmic_grain_info(input_data=None):
    # This is where your Tabelul Numeric Universal logic would go.
    # For now, we'll return a simple, relevant message.
    if input_data:
        return f"Cosmic Grain processed '{input_data}' from Hunedoara, Romania. Output based on your numeric paradigm. (Mock AI response)"
    return "Welcome to Cosmic Grain from Hunedoara, Romania! Send some data to process."

@app.route('/')
def home():
    return get_cosmic_grain_info()

@app.route('/process', methods=['POST'])
def process_data():
    data = request.json.get('data') if request.json else request.args.get('data')
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    # Here you could integrate with a real Google AI model (like Gemini)
    # For now, it's a mock response showing integration intent.
    ai_response = f"AI says: Processing '{data}' with Cosmic Grain logic. Result is a new numeric insight."
    
    return jsonify({
        "input": data,
        "cosmic_grain_output": get_cosmic_grain_info(data),
        "ai_integration_mock": ai_response
    })

if __name__ == '__main__':
    # Cloud Run/GKE typically set the PORT environment variable
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)


