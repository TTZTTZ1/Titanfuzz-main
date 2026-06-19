import torch
input_tensor = torch.tensor([False, True, False])
result = torch.any(input_tensor)
print(result)