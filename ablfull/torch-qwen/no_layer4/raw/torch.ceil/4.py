import torch

input_data = torch.tensor([-1.7, -1.5, -0.2, 0.3, 1.8])
result = torch.ceil(input_data)
print(result)