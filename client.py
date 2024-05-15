from model.trainer import model_train
from utils.reader import model_config,inference_config
from inference import generate_text
import sys
# print(sys.path)

if __name__=="__main__":
    text = 'Keep your healthcare card open quickly'
    # inference_config['max_length'] = 100
    print(f"max_length:{inference_config['max_length']}")
    if model_config['use_trainer'] is True:
        model_train(model_config)

    rtn = generate_text(text)
    print(rtn)