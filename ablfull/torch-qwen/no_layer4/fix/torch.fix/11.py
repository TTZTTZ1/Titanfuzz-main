import torch
input_tensor = torch.tensor([(- 1.5), 0.5, 2.5], dtype=torch.float32)
result = torch.fix(input_tensor)