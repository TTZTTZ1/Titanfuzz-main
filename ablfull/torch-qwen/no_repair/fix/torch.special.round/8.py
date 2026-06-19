
import torch
input_data = torch.tensor([1.5, (- 0.4), 2.7], dtype=torch.float)
result = torch.special.round(input_data)
print(result)
