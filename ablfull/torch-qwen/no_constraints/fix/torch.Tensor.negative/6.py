import torch
input_tensor = torch.tensor([1.0, (- 2.0), 3.0])
result_tensor = torch.Tensor.negative(input_tensor)
print(result_tensor)