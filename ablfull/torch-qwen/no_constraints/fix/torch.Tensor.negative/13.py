import torch
input_data = torch.rand(3, requires_grad=True)
result = input_data.negative()