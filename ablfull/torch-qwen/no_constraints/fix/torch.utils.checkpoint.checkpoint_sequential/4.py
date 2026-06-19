import torch

def my_function(x):
    return (((x * x) + x) + 1)
input_data = torch.randn(10)
output = torch.utils.checkpoint.checkpoint_sequential([my_function], 1, input_data)
print(output)