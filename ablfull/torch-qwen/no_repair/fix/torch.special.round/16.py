
import torch
input_tensor = torch.tensor([1.5, (- 0.3), 4.7])
result = torch.special.round(input_tensor)
print(result)
