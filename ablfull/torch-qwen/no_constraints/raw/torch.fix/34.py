import torch

input_tensor = torch.tensor([-1.5, 0.3, 2.7], dtype=torch.float32)
result = torch.fix(input_tensor)
print(result)