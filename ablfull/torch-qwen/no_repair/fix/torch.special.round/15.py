
import torch
input_tensor = torch.tensor([0.5, (- 1.2), 3.7])
result = torch.special.round(input_tensor)
print(result)
