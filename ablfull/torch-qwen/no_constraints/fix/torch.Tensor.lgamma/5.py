import torch
input_data = torch.tensor([0.5])
result = torch.Tensor.lgamma(input_data)
print(result)