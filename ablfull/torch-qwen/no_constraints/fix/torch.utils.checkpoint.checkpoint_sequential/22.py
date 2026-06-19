import torch

def my_function(x):
    return (((x * x) + (2 * x)) + 1)
functions = [my_function]
input_data = torch.randn(5)
output = torch.utils.checkpoint.checkpoint_sequential(functions, segments=1, input=input_data)