import torch
input_tensor = torch.tensor([[False, False], [True, True]])
result = torch.any(input_tensor)
print(result)