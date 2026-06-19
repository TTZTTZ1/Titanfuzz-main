import torch

def simple_function(x):
    return (((x * x) + (2 * x)) + 1)
functions = ([simple_function] * 3)
input_data = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
output = torch.utils.checkpoint.checkpoint_sequential(functions, segments=1, input=input_data)
print(output)