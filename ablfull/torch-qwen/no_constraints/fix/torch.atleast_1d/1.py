import torch
input_data = [torch.tensor(1), torch.tensor(2), torch.tensor(3)]
result = torch.atleast_1d(*input_data)
print(result)