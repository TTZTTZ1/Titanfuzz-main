
import torch
input_tensor = torch.tensor([1.5, (- 2.3), 0.8])
result = torch.special.round(input_tensor)
print(result)
