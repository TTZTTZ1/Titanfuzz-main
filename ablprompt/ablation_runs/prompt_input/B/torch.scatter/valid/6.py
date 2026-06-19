import torch

# Create a random input tensor
input_tensor = torch.randn(5, 5)

# Create a random index tensor
index_tensor = torch.randint(0, 5, (5, 5))

# Create a source tensor with the same shape as the index tensor
source_tensor = torch.randn(5, 5)

# Perform scatter operation
output_tensor = torch.scatter(input_tensor, 0, index_tensor, source_tensor)

print(output_tensor)