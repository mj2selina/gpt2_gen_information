from transformers import Trainer,TrainingArguments
from transformers import GPT2Tokenizer,GPT2LMHeadModel
from model.loader import *

def model_train(config):
    tokenizer = GPT2Tokenizer.from_pretrained(config['model_name'])
    train_dataset = load_dataset(config['train_file_path'],tokenizer)
    data_collator = load_data_collator(tokenizer)
    tokenizer.save_pretrained(config['output_dir'])
    model = GPT2LMHeadModel.from_pretrained(config['model_name'])

    model.save_pretrained(config['output_dir'])

    training_args = TrainingArguments(
        output_dir = config['output_dir'],
        overwrite_output_dir=config['overwrite_output_dir'],
        per_device_train_batch_size=config['per_device_train_batch_size'],
        num_train_epochs=config['num_train_epochs'],
    )

    trainer = Trainer(
        model = model,
        args = training_args,
        data_collator=data_collator,
        train_dataset=train_dataset
    )

    trainer.train()
    trainer.save_model()


    
    