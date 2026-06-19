
import torch
input_data = torch.tensor([0.5, (- 0.7), 2.3])
result = torch.special.round(input_data)
print(result)
