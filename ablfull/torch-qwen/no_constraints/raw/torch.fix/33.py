import torch

input_data = torch.tensor([-0.7, -0.3, 0.2, 0.6])
result = torch.fix(input_data)
print(result)