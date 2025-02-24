import torch
from transformers import BertTokenizer, BertForSequenceClassification

MODEL_PATH = "../models/bert_finetuned"



def load_model():
    """Load the fine-tuned model and tokenizer."""
    tokenizer = BertTokenizer.from_pretrained(MODEL_PATH)
    model = BertForSequenceClassification.from_pretrained(MODEL_PATH)

    # Ensure the model is on the correct device
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)
    model.eval()

    return model, tokenizer, device

def predict_text(text, model, tokenizer, device):
    """Make a prediction on the given text."""
    encodings = tokenizer(
        text,
        max_length=128,
        padding='max_length',
        truncation=True,
        return_tensors='pt'
    )
    input_ids = encodings['input_ids'].to(device)
    attention_mask = encodings['attention_mask'].to(device)

    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask)
        probabilities = torch.softmax(outputs.logits, dim=1)
        prediction = torch.argmax(probabilities, dim=1).item()
        confidence = probabilities[0][prediction].item()

    return prediction, confidence
