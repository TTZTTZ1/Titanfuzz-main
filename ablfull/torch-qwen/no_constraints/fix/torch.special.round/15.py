import torch
x = torch.tensor([(- 2.5), (- 1.4), 0.0, 1.6, 2.5], dtype=torch.float32)
result = torch.special.round(x)
print(result)