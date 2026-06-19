import torch

# Create a complex tensor
input_tensor = torch.tensor([0.0, torch.pi/2, torch.pi], dtype=torch.float32)

# Compute the cosine of each element
output_tensor = torch.cos(input_tensor)

print(output_tensor)