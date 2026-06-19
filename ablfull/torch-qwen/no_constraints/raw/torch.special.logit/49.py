import torch

input_tensor = torch.tensor([0.5], dtype=torch.float32)
result = torch.special.logit(input_tensor)