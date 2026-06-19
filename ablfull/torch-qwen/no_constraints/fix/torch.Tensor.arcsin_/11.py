import torch
input_tensor = torch.tensor([0.5])
result = torch.Tensor.arcsin_(input_tensor)
print(result)