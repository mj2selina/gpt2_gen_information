from utils.reader import model_config,inference_config
from model.loader import load_model,load_tokenizer

def generate_text(sequence):
    model_path = model_config['output_dir']
    model = load_model(model_path=model_path)
    tokenizer = load_tokenizer(model_path)

    ids = tokenizer.encode(f'{sequence}',return_tensors='pt')
    final_outputs =  model.generate(
        ids,
        do_sample=True,
        max_length=inference_config['max_length'],
        pad_token_id=model.config.eos_token_id,
        top_k=50,
        top_p=0.95,
    )
    gen_data = tokenizer.decode(final_outputs[0],skip_special_tokens=True)
    gen_data_list = gen_data.split('.')[:-1]
    return '.'.join(gen_data_list) + '.'
