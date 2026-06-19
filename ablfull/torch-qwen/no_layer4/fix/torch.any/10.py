import torch
input_tensor = torch.tensor([[(- 1.0), (- 0.5)], [0.0, 0.5]])
result = torch.any(input_tensor, dim=1)
print(result)