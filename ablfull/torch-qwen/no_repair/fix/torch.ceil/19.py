
import torch
input_tensor = torch.tensor([(- 1.5), 0.0, 1.5], dtype=torch.float)
result = torch.ceil(input_tensor)
print(result)
