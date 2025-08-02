## Steps: 
## Load dataset -> Data Preprocessing (lowercasing) -> Split dataset (training, validation, test)
## -> Tokenization using BERT Tokenizer to convert text to BERT-compatible tokens
## -> model training, train BERT on phishing email data -> Evaluation on Test Dataset
## -> if the eval is not good, train the model again -> if good, Model saving, save trained 
## and tokenizer -> Model Deployement, expose model through API or web interface for predictions