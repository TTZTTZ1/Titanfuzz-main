import torch
from torch.nn import Sequential, Linear

# Prepare the data
model = Sequential(Linear(10, 5), Linear(5, 1))
input_tensor = torch.randn(1, 10)

# Call the API
output = torch.utils.checkpoint.checkpoint_sequential(model, segments=2, input=input_tensor)
print(output.shape)