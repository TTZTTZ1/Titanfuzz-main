import torch
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]], dtype=torch.float64)
result = torch.slogdet(input_tensor)
print(result)