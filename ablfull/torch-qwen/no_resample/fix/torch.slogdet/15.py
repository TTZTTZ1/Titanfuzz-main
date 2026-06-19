import torch
input_data = torch.randn(3, 3, dtype=torch.float)
result = torch.slogdet(input_data)