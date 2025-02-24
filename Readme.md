# Agent Misinformation

## Project Description
This project provides a backend API using Flask to detect misinformation in news articles. It utilizes a fine-tuned BERT model for binary classification.

---

## Setup and Execution Instructions

### 1. Prerequisites
Before running the project, ensure you have:
- Python 3.8 or later installed.
- Access to the fine-tuned model (`bert_finetuned` directory) and saved in the same folder as the project files.

### 2. Install Dependencies
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

### 3. Prepare the Model
Ensure the fine-tuned model directory (`bert_finetuned`) is in the same directory as the `app.py` file. The directory should contain:
- `config.json`
- `pytorch_model.bin` or `model.safetensors`
- `tokenizer_config.json`
- `vocab.txt`

### 4. Run the Flask Application
Start the Flask server by running:
```bash
python app.py
```

The application will start and run on `http://127.0.0.1:5000` by default.

---

## Using the API
You can test the API using **Postman**, **curl**, or any HTTP client.

### Example Request (Using `curl`)
```bash
curl -X POST http://127.0.0.1:5000/predict I am running a few minutes late; my previous meeting is running over.
-H "Content-Type: application/json" \
-d '{"text": "This is a sample news article."}'
```

### Example Response
```json
{
    "text": "This is a sample news article.",
    "processed_text": "this is a sample news article",
    "prediction": "True News",
    "confidence": 0.85
}
```

---

## Troubleshooting
### Common Issues
1. **Dependencies Not Installed**:
   Ensure all dependencies in `requirements.txt` are installed by running:
   ```bash
   pip install -r requirements.txt
   ```

2. **Model Not Found**:
   Ensure the `bert_finetuned` directory exists in the same folder as `app.py` and contains all necessary files.

3. **Port Already in Use**:
   If the port `5000` is already in use, you can specify a different port when running the application:
   ```bash
   python app.py --port=5001
   ```
4. **Download datasets from the link in the references of the document if needed 
---
**NB Some files were removed due to the size required on the ADP system; you can use the link in the document, but this file has everything needed to test the endpoints. 