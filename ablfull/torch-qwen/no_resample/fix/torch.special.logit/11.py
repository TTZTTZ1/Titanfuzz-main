import torch
input_data = torch.tensor([(- 1.0), 0.5, 1.0])
result = torch.special.logit(input_data)