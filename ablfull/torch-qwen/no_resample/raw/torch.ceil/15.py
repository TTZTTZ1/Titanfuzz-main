import torch

input_tensor = torch.tensor([-1.5, -0.2, 0.7, 1.3], dtype=torch.float)
result = torch.ceil(input_tensor)
print(result)