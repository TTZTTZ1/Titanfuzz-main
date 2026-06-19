import torch

# Create a sample input tensor
input_tensor = torch.randn(3, 4)

# Create a sample index tensor
index_tensor = torch.randint(0, 4, (3, 4))

# Use torch.gather to select elements
output_tensor = torch.gather(input_tensor, 1, index_tensor.unsqueeze(-1).expand(-1, -1, 4))

print(output_tensor)