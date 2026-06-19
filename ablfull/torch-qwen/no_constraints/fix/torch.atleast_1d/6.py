import torch
input_data = 42
result = torch.atleast_1d(torch.tensor([input_data]))
print(result)