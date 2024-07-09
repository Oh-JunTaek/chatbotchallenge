from flask import Flask, request, jsonify, render_template
from transformers import GPT2LMHeadModel, PreTrainedTokenizerFast
import torch

app = Flask(__name__)

model_name = "skt/kogpt2-base-v2"
tokenizer = PreTrainedTokenizerFast.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    user_message = data.get('message')

    if user_message is None:
        return jsonify({'response': 'No message provided'}), 400
    
    inputs = tokenizer.encode(user_message + tokenizer.eos_token, return_tensors="pt")
    outputs = model.generate(inputs, max_length=50, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(outputs[:, inputs.shape[-1]:][0], skip_special_tokens=True)
    
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(port=5000)