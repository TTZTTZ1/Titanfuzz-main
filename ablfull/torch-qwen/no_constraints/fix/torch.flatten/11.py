import torch
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
flattened_tensor = torch.flatten(input_tensor)
print(flattened_tensor)