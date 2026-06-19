import torch
input_tensor = torch.tensor([1.5, (- 0.7), 2.3])
output_tensor = torch.special.round(input_tensor)
print(output_tensor)