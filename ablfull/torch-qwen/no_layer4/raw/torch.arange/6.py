import torch

input_data = {
    'start': 0,
    'end': 5,
    'step': 1
}

result = torch.arange(**input_data)