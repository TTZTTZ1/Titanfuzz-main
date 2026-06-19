
import torch
input_data = torch.tensor([0.5, 1.0, 2.0], dtype=torch.float32)
output_data = torch.special.psi(input_data)
print(output_data)
