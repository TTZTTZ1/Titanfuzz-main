import torch
input_data = torch.tensor([0.5, (- 0.5), 0.0])
result = torch.Tensor.sin(input_data)
print(result)