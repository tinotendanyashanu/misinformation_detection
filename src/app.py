from flask import Flask, request, jsonify
from model import load_model, predict_text
from preprocess import preprocess_text

# Initialize Flask app
app = Flask(__name__)

# Load model and tokenizer
model, tokenizer, device = load_model()

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the request
        data = request.json
        text = data.get('text')
        if not text:
            return jsonify({'error': 'No text provided for prediction'}), 400

        # Preprocess the text
        processed_text = preprocess_text(text)

        # Get prediction and confidence
        prediction, confidence = predict_text(processed_text, model, tokenizer, device)

        # Return response
        return jsonify({
            'text': text,
            'processed_text': processed_text,
            'prediction': 'True News' if prediction == 1 else 'False News',
            'confidence': confidence
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
