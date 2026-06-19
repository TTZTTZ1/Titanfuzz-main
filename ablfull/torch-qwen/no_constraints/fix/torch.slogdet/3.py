import torch
input_tensor = torch.tensor([[4.0, 0.0], [0.0, 3.0]])
result = torch.slogdet(input_tensor)
print(result)