
import torch
input_data = torch.tensor([0.1, 0.4, 0.6, 0.9], dtype=torch.float)
result = torch.special.logit(input_data)
