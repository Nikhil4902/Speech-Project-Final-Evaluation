import json
import torch
from importlib import import_module
from models.AASIST import HtrgGraphAttentionLayer, GraphPool, GraphAttentionLayer, CONV, Residual_block, Model
from main import get_model

def load_and_print_model_architecture(model_path):
    with open("config/AASIST-L.conf", 'r') as f_conf:
        conf = json.loads(f_conf.read())
        m_conf = conf["model_config"]
    # Create an instance of the model
    model: torch.nn.Module = get_model(m_conf, torch.device("cpu"))  # Update with the actual model class
    # module = import_module(f"models.{m_conf['model_architecture']}")
    # getattr(module, "Model")

    # Load pretrained weights
    model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
    # print(model)
    i = 0
    for p in model.parameters():
        print(p.shape)
        i+=1
    print(f"\n\n\n\n\nNum Model Parameters: {i}\n\n\n\n\n")
    

    # Print model architecture
 
         
    k = 0
    j = 0
    for m in model.modules():
        print(m)
        if not isinstance(m, (torch.nn.Sequential, HtrgGraphAttentionLayer, GraphPool, GraphAttentionLayer, CONV, Residual_block, Model)):
            i = 0
            for p in m.parameters():
                print("New Param")
                print(p.shape)
                i+=1        # if not isinstance(m, torch.nn.Sequential):
                # print(m)
            k += i
            print("*"*100,i,'*'*100,sep='\n')
            j+=1
    print(f"\n\n\n\n\n\n\nNum Modules: {j}, {k}\n\n\n\n\n\n")


pretrained_model_path = "models/weights/AASIST-L.pth"
load_and_print_model_architecture(pretrained_model_path)
