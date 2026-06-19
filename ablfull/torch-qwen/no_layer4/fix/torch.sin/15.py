import torch
input_tensor = torch.tensor([0.5, (- 0.3)], dtype=torch.float)
result = torch.sin(input_tensor)
print(result)