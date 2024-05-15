from utils.cleaner import cleaning
import yaml


def read_config(config_path):
    with open(config_path,'r',encoding='utf-8') as f:
        datas = yaml.load(f,Loader=yaml.FullLoader)
    return datas


def read_data(path):
    text_data = []
    with open(path,'r') as f:
        for line in f:
            text_data.append(cleaning(line))
    return text_data

config_path = '/Users/jun/LLM/gpt2_gen_misinformation/config/model_config.yaml'
model_config = read_config(config_path)

inference_config_path = '/Users/jun/LLM/gpt2_gen_misinformation/config/inference_config.yaml'
inference_config = read_config(inference_config_path)