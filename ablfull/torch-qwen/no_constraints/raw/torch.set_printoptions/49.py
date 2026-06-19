import torch

input_data = {
    'precision': None,
    'threshold': None,
    'edgeitems': None,
    'linewidth': None,
    'profile': None,
    'sci_mode': False
}

torch.set_printoptions(**input_data)