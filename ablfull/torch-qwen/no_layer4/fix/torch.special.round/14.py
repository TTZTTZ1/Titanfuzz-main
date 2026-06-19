import torch
input_data = torch.tensor([1.5, (- 2.3), 4.7], dtype=torch.float)
result = torch.special.round(input_data)