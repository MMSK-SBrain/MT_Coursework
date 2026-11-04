# Customer Support Chatbot

A production-ready chatbot for customer support using intent classification and natural language processing.

## Features

- **15+ Supported Intents**: Greeting, order tracking, returns, payments, shipping, and more
- **High Accuracy**: >90% intent classification accuracy
- **Natural Responses**: Template-based response generation with randomization
- **Real-time Chat**: Interactive Streamlit interface
- **Confidence Scoring**: Shows prediction confidence for each response

## Project Structure

```
customer-support-chatbot/
├── app.py                    # Streamlit web application
├── chatbot-training.ipynb    # Training notebook
├── intents.json             # Intent definitions
├── requirements.txt         # Python dependencies
├── README.md               # This file
├── intent_classifier.pkl   # Trained model (generated)
└── tfidf_vectorizer.pkl   # Vectorizer (generated)
```

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Train the Model

Open and run `chatbot-training.ipynb` to:
- Load intent data
- Train the intent classifier
- Generate and save models

This will create:
- `intent_classifier.pkl`
- `tfidf_vectorizer.pkl`

### 3. Run the Chatbot

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Usage

1. Type your question in the chat input
2. Click "Send" or press Enter
3. The bot will:
   - Classify your intent
   - Generate an appropriate response
   - Show confidence score

### Example Queries

- "Where is my order?"
- "I want to return this product"
- "What are your business hours?"
- "Do you have any promo codes?"
- "My payment didn't go through"

## Model Performance

- **Accuracy**: >90% on test set
- **Intents**: 15 categories
- **Training Samples**: ~120 patterns
- **Algorithm**: Logistic Regression with TF-IDF

## Deployment

### Streamlit Cloud (Free)

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Deploy!

### Heroku

```bash
# Add Procfile
echo "web: streamlit run app.py --server.port=$PORT" > Procfile

# Deploy
git init
heroku create your-chatbot-name
git push heroku main
```

## Customization

### Add New Intents

Edit `intents.json`:

```json
{
  "tag": "new_intent",
  "patterns": [
    "Example question 1",
    "Example question 2"
  ],
  "responses": [
    "Response 1",
    "Response 2"
  ]
}
```

Then retrain the model.

### Improve Responses

1. Add more response variations in `intents.json`
2. Integrate with APIs for dynamic data (order status, etc.)
3. Add entity extraction for specific information

## Future Enhancements

- [ ] Add context management for multi-turn conversations
- [ ] Integrate with database for real order tracking
- [ ] Add entity extraction (order numbers, dates, etc.)
- [ ] Implement fallback to human agent
- [ ] Add multilingual support
- [ ] Track conversation analytics

## Troubleshooting

**Issue**: Models not found  
**Solution**: Run `chatbot-training.ipynb` first to generate models

**Issue**: Low accuracy  
**Solution**: Add more training patterns in `intents.json`

**Issue**: Streamlit won't start  
**Solution**: Check if port 8501 is available: `lsof -i :8501`

## License

Created for ML for Engineers Course - 2026

## Contact

For questions or issues, refer to course materials or instructor.
