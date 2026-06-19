import torch

input_data = torch.tensor([-1.5, -0.4, 0.0, 0.6, 1.2])
result = torch.fix(input_data)
print(result)