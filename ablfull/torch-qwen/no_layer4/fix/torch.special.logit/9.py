import torch
input_data = torch.tensor([(- 0.5), 0.0, 0.5], dtype=torch.float)
result = torch.special.logit(input_data)