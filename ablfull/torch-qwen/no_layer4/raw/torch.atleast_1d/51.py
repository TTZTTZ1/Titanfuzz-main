import torch

input_tensor = torch.tensor(5)
result = torch.atleast_1d(input_tensor)
print(result)