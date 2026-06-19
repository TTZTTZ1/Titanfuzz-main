import torch

input_tensor = torch.tensor([0.5], dtype=torch.float32)
result = input_tensor.arcsin_()
print(result)