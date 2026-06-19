import torch
input_data = torch.tensor([0.0, 1.0, 2.0], dtype=torch.float)
output_data = torch.sin(input_data)
print(output_data)