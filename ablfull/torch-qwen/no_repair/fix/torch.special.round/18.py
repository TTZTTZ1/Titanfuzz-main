
import torch
input_tensor = torch.tensor([1.5, (- 2.3), 4.8])
output_tensor = torch.special.round(input_tensor)
print(output_tensor)
