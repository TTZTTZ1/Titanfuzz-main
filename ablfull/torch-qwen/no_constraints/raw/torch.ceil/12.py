import torch

input_data = torch.tensor([-1.7, 2.0, 3.5], dtype=torch.float32)
result = torch.ceil(input_data)
print(result)