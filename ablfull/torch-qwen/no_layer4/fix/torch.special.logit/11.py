import torch
input_tensor = torch.tensor([0.5, 0.75, 0.8], dtype=torch.float)
result = torch.special.logit(input_tensor)