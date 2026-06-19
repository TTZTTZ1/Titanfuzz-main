import torch

input_data = torch.tensor([-1.5, -0.3, 0.7, 1.2], dtype=torch.float32)
result = torch.ceil(input_data)
print(result)