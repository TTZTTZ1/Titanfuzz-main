import torch

# Create a 3D tensor
input_tensor = torch.randn(2, 3, 4)

# Create an index tensor
index_tensor = torch.randint(0, 3, (2, 3))

# Use torch.gather to gather elements
output_tensor = torch.gather(input_tensor, 1, index_tensor.unsqueeze(-1).expand(-1, -1, 4))

print(output_tensor)