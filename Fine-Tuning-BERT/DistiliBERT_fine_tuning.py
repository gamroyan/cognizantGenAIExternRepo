from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification
from transformers import Trainer, TrainingArguments
from datasets import load_dataset
import torch

# Load the IMDb dataset
dataset = load_dataset('imdb')

# Load the DistilBERT tokenizer
tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased')

# Tokenize the dataset
def tokenize_function(examples):
    return tokenizer(examples['text'], padding="max_length", truncation=True, max_length=128)

tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Prepare data for PyTorch
tokenized_datasets = tokenized_datasets.rename_column("label", "labels")
tokenized_datasets.set_format("torch", columns=["input_ids", "attention_mask", "labels"])

# Use a subset for faster training
train_dataset = tokenized_datasets["train"].shuffle(seed=42).select(range(2000))
test_dataset = tokenized_datasets["test"].shuffle(seed=42).select(range(500))

# Load the DistilBERT model
model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=2)

# Define training arguments
training_args = TrainingArguments(
    output_dir="./distilbert-results",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=2,  # reduced from 3 to 2, for faster training
    weight_decay=0.01,
    logging_dir='./distilbert-logs',
    logging_steps=10,
    save_steps=10,
    evaluation_strategy="epoch"
)

# Define Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
)

# Train the model
trainer.train()

# Evaluate the model
eval_result = trainer.evaluate()
print(f"DistilBERT Evaluation results: {eval_result}")