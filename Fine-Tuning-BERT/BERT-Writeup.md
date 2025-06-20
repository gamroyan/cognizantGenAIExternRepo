# Fine-Tuning BERT Project with HuggingFace
This project fine-tunes a ```bert-base-uncased``` model for binary sentiment classification on the IMDb movie review dataset using the HuggingFace Transformers library.

## Part 1: Fine-Tuning BERT
**NLP Task:** sentiment analysis (Positive vs. Negative IMDb Movie Reviews)

**Model:** ```BertForSequenceClassification``` for binary classification

**Dataset:** IMDb (via Hugging Face Datasets library)

**Key Hyperparameters:**
- Batch size: 16
- Learning rate: 2e-5
- Epochs: 3
- Evaluation strategy: per epoch
- Weight decay: 0.01

Logging and checkpoint saving enabled every 10 steps

**Training:** Used Hugging Face's ```Trainer``` API to set up a training loop for training and evaluation of the model.

### Files
- ```fine_tuning_bert.py```: main script to tokenize data, fine-tune BERT, and evaluate the model.
- ```results/```: contains training checkpoints and logs (full directory is ```.gitignored``` becuase of size. I pulled a few example checkpoints' trainer states for analysis)

### Results
Each entry (checkpoints) in ```results``` gives a snapshot of training at a particular step.

The model was fine-tuned for 3 epochs, reaching a total of 375 training steps. As we can see through the logs, loss steadily declined from an initial value of 0.6997 to a final low of 0.0843 at step 280, with minor fluctuations in later stages. The lowest loss was reached just past the 2-epoch mark, after which loss values hovered in the 0.1–0.2 range. This shows that the model was likely making confident and correct predicitons around this time.

**Loss Projection (sampled from a few steps):**
|Step|Epoch|Loss|
|---|---|---|
|10|0.08|0.6997|
|50|0.40|0.4242|
|100|0.80|0.4233|
|150|1.20|0.2240|
|200|1.60|0.2777|
|250|2.00|0.2279|
|280|2.24|0.0843 (lowest)|
|370|2.96|0.1228|

The learning rate followed a linear decay schedule, starting at 1.95e-5 to 3.2e-7 by the final step. With a learning rate that decreased over the course of training, the model was able to explore more broadly initially, then fine-tune carefully later on. Gradient norms stayed mostly within expected bounds, but some spikes were observed (e.g. 15.03 at step 70) which were most likely corresponding to noisier batches.

Overall, the training progression shows that the model learned effectively. The results support the decision to train for only approximately 2–3 epochs since most of the performance gains occurred early in training and slowly leveled out during the 3-epoch mark.

**Lowest point of loss we achieved in ```/results/checkpoint-375/trainer_state.json```:**
![alt text][logo]

[logo]:https://github.com/gamroyan/cognizantGenAIExternRepo/blob/main/Fine-Tuning-BERT/BERT%20Fine-Tuning%20Checkpoint375.png "Checkpoint 375"


## Part 2: Debugging Issues

## Part 3: Evaluating the Model

## Part 4: Creative Application
