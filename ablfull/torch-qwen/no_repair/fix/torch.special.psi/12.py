
import torch
input_data = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)
result = torch.special.psi(input_data)
print(result)
