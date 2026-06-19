import torch
input_data = torch.tensor([5, 6, 7])
result = torch.atleast_1d(input_data)
print(result)