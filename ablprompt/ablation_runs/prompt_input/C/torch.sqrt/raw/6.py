import torch

input_tensor = torch.tensor([4.0, 9.0, 16.0], dtype=torch.float32)
output_tensor = torch.sqrt(input_tensor)
print(output_tensor)