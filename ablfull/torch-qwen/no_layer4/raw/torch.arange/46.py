import torch

input_data = {
    'start': 0,
    'end': 5,
    'step': 1,
    'dtype': None,
    'layout': None,
    'device': None,
    'requires_grad': False
}

result = torch.arange(**input_data)
print(result)