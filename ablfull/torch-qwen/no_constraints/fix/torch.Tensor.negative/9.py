import torch
input_tensor = torch.tensor([1, (- 2), 3], dtype=torch.float32)
result = torch.Tensor.negative(input_tensor)