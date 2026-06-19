
import torch
input_data = torch.tensor([0.5, (- 0.5)], dtype=torch.float)
output = torch.sin(input_data)
print(output)
