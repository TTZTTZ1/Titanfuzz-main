import torch
input_tensor = torch.tensor([[False, True], [False, False]])
dim = 1
result = torch.any(input_tensor, dim=dim)
print(result)