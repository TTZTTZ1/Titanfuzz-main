import torch
input_tensor = torch.tensor([[False, True], [False, False]])
result = torch.any(input_tensor)
print(result)