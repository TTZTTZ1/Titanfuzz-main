import torch

input_tensor = torch.randn(5)
result = torch.std_mean(input_tensor, dim=0, correction=1, keepdim=False)