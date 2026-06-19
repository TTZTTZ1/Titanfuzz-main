import torch
input_data = torch.tensor(42)
result = torch.atleast_1d(input_data)
print(result)