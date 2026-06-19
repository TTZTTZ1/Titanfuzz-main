import torch

input_data = torch.tensor([-1.5, -0.5, 0.5, 1.5])
result = torch.fix(input_data)
print(result)