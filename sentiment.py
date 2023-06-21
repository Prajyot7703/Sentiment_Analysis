from transformers import pipeline
sent_pipeline = pipeline("sentiment-analysis")

sent_pipeline('I love sentiment analysis!')

sent_pipeline('Booo')
print(sent_pipeline('It tastes awesome'))
print(sent_pipeline('Booo')[0]["label"])