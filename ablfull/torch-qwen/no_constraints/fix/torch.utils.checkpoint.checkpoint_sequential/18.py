import torch
from torch.utils.checkpoint import checkpoint_sequential

def simple_function(x):
    return (((x * x) + (2 * x)) + 1)
input_data = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
result = checkpoint_sequential((simple_function,), 1, input_data)
print(result)