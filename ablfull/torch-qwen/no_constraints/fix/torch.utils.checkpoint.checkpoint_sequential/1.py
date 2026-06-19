import torch

def func(x):
    return (((x * x) + (2 * x)) + 1)
input_data = torch.randn(5)
result = torch.utils.checkpoint.checkpoint_sequential([func], 1, input_data)
print(result)