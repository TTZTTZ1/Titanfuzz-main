
import torch
input_data = torch.tensor([0.1, 0.4, 0.7], dtype=torch.float32)
result = torch.special.logit(input_data)
