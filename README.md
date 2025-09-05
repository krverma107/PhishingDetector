# PhishingDetector
AI Powered Phishing Detector
Project Overview
This project implements a BERT-based phishing email classifier that detects whether an email is phishing (1) or legitimate (0) based on its text. The model is fine-tuned from a pre-trained BERT architecture using the Hugging Face transformers library. It follows the full NLP pipeline: Corpus selection (labeled phishing/legitimate emails) Text preprocessing and cleaning Tokenization with BERT’s tokenizer Model selection and fine-tuning Evaluation with standard metrics (Accuracy, Precision, Recall, F1-score)

Installation Instructions
This project uses Python 3.8+ and the following key packages:

transformers>=4.30.0

torch>=2.0.0

pandas>=1.5.0

numpy>=1.24.0

scikit-learn>=1.2.0
 
matplotlib>=3.7.0

1. Download the .ipnyb file containing the code.
2. Install the required packages

Dataset
The project uses a public dataset (cited in the report) Follow this link: https://www.kaggle.com/datasets/naserabdullahalam/phishing-email-dataset, scroll down and on the right side download the csv file titled "phishing_email.csv".

How to run the code
Running the code is straight forward after all the packages have been downloaded. I used Google Colab Pro which took about 2 hours to train the model. Run each code section and make sure no errors occur before moving on. Once you are at the

trainer.train

section, the code will take a while to run. During training, you will see an output table like: Screenshot 2025-08-10 at 7.18.33 PM.png

Expected Output
After training:

Loss vs Epochs and Accuracy vs Epochs plots will be displayed.
A classification report with Precision, Recall, and F1-scores for each class.
A confusion matrix showing correct and incorrect predictions.
