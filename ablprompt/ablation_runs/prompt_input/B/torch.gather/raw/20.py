import torch

# Create a 3D tensor
input_tensor = torch.randn(2, 3, 4)

# Create an index tensor with the same shape as the input tensor but with long data type
index_tensor = torch.randint(0, 4, (2, 3, 4))

# Use torch.gather to gather elements along the last dimension (dim=2)
output_tensor = torch.gather(input_tensor, 2, index_tensor.unsqueeze(-1).expand_as(input_tensor))

print(output_tensor)