import torch
input_data = torch.tensor([0.5, 1.0, 2.0])
result = torch.Tensor.lgamma(input_data)
print(result)