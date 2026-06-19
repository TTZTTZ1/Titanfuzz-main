import torch
input_tensor = torch.tensor([[[[0.456]]], [[[0.789]]]])
flattened_tensor = torch.flatten(input_tensor)
print(flattened_tensor)