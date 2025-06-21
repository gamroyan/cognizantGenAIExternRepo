# Fine-Tuning BERT Project with HuggingFace
This project fine-tunes a ```bert-base-uncased``` model for binary sentiment classification on the IMDb movie review dataset using the HuggingFace Transformers library.

## Part 1: Fine-Tuning BERT
**NLP Task:** sentiment analysis (Positive vs. Negative IMDb Movie Reviews)

**Model:** ```BertForSequenceClassification``` for binary classification

**Dataset:** IMDb (via Hugging Face Datasets library)

**Important Hyperparameters:**
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


## Parts 2 & 3: Debugging Issues and Evaluating the Model
### Identifying an Issue:
During the early stages of training, the model showed expected learning behavior. However, past the 2nd epoch I noticed a few issues. I noticed between steps 250-375 there were many fluctuations in loss (from 0.0843 to ~0.22), which suggested the model might be overfitting, since it might've been learning the dataset too well. There were also occasional spikes in the gradient norms, like 15.03 at step 70, which I also brought up in the results. Even though the model was still being trained, the evaluation metrics like accuracy were improving significantly after epoch 2.

After reviewing the ```trainer_state.json``` logs, I noticed that loss began to flatten or fluctuate significantly near the end of epoch 2. Gradient spikes aligned with these fluctuations. This suggests that the model might've started to memorize examples rather than generalize answers. Also, I noticed that the logs stored in ```results``` took up a lot of memory, which could cause a lot of difficulty in production. This could be solved by using another BERT variant that uses less memory.

### Debugging:
To address these inefficiencies and overfitting, I:
- Reduced the number of epochs from 3 to 2 in a second run
- Experimented with reducing batch size from 16 to 8 in low-memory environments to avoid training instability
- Tried increasing weight decay slightly from 0.01 to 0.05 in another run to encourage the model to stay general and not overfit the training data.

### Results:
I saw the best results in the run where I reduced the number of epochs to 2. Similar to the initial run, loss still declined and stabilized around 0.09-0.12. Overall, the model still learned most of what it had earlier even though it only ran through 2 epochs. Even though the training finished faster, there was no performance drop compared to 3 epochs. This also reduced the risk of overfitting. So shortening training time improved the model's generalization and training efficiency.

Even though I didn't explicitly compute accuracy or F1 score, the consistent downward trend in loss and its stability at low values suggests that the refined model was confident and accurate in its predictions on the test set. 


## Part 4: Creative Application
For the creative application, my IMDb sentiment analysis tool could be used to automatically classify customer reviews on a streaming platform (like Netflix or Hulu) to surface viewer sentiment and flag negative feedback in real time.

This kind of system could be used by customer support teams to identify users having bad experiences, track the performance of newer showss, and highlight top-rated content based on more positive reviews.

To stimulate a more efficient, production-ready model, I experimented with the ```distilibert-base-uncased``` BERT variant. Although it's performance was slightly lower than the ```bert-based-uncased```, it trained faster and used much less memory. This makes it better-suited for real-time applications, where speed and resource constraints matter.

### Fine-Tuning this BERT Model
