import torch
input_tensor = torch.randn(4, 3, 2)
flattened_tensor = torch.flatten(input_tensor)
print(flattened_tensor)