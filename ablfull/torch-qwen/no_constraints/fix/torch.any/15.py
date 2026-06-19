import torch
tensor = torch.tensor([True, False, True])
result = torch.any(tensor)
print(result)