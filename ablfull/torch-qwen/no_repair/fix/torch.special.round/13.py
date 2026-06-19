
import torch
input_tensor = torch.tensor([1.5, (- 0.4), 2.8], dtype=torch.float)
result = torch.special.round(input_tensor)
print(result)
