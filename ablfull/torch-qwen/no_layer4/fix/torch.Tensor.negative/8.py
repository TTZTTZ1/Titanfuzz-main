import torch
input_data = torch.tensor([1.0, (- 2.0), 3.0])
result = torch.Tensor.negative(input_data)
print(result)