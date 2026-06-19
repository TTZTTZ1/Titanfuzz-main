import torch

def dummy_function(x):
    return x * 2

input_data = torch.randn(10)
result = torch.utils.checkpoint.checkpoint_sequential([dummy_function], 2, input_data)