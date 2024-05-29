# create virtual environment
# conda create --name train transformers transformers[torch]  accelerate --channel conda-

# anti-trans/
# - train.py [this file]
# - train.csv
# - (baby)

import torch
from datasets import load_dataset
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    TrainingArguments,
    pipeline,
    logging,
)
from trl import SFTTrainer

tokenizer = AutoTokenizer.from_pretrained("./mistral7/")
model = AutoModelForCausalLM.from_pretrained("./mistral7/")
dataset = load_dataset("csv", data_files="/scratch/network/fc1991/train.csv", trust_remote_code=True)tokenizer = AutoTokenizer.from_pretrained("./mistral7/")
model = AutoModelForCausalLM.from_pretrained("./mistral7/")
dataset = load_dataset("csv", data_files="/scratch/network/fc1991/train.csv", trust_remote_code=True)

tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"
torch.device('cuda:0')
model.to('cuda')

training_params = TrainingArguments(
    output_dir="./results",
    num_train_epochs=5,
    # per_device_train_batch_size=4, # defaults to 8, but should lower if memory issues
    # gradient_accumulation_steps=1,
    # save_steps=25,
    # logging_steps=25,
    learning_rate=2e-4,
    weight_decay=0.001,
)

trainer = SFTTrainer(
    model=model,
    train_dataset=dataset['train'],
    dataset_text_field="definitions",
    max_seq_length=None,
    tokenizer=tokenizer,
    args=training_params,
    packing=False,
)

trainer.model.save_pretrained("model")
trainer.tokenizer.save_pretrained("tokenizer")

trainer.train()

tokenizer.save_pretrained('/scratch/network/fc1991/baby')
trainer.save_model('/scratch/network/fc1991/baby', 'pytorch_model')
