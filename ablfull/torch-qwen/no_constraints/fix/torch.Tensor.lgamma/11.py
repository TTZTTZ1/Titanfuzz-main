import torch
input_data = torch.tensor([1.0, 2.5, 4.0])
result = torch.Tensor.lgamma(input_data)
print(result)