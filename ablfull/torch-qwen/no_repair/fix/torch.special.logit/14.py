
import torch
input_data = torch.tensor([0.5, 0.7, 0.3], dtype=torch.float)
result = torch.special.logit(input_data)
