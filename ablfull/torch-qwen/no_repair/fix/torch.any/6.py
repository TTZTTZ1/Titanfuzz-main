
import torch
input_tensor = torch.tensor([[True, False], [False, True]])
result = torch.any(input_tensor)
print(result)
