import torch

input_data = {
    'start': 0,
    'end': 5,
    'step': 1,
    'dtype': torch.int,
    'device': torch.device('cpu'),
    'requires_grad': False
}

result = torch.arange(**input_data)