import torch

# Create a random input tensor
input_tensor = torch.randn(4, 5)

# Create a random index tensor
index_tensor = torch.randint(0, 5, (4,))

# Create a random source tensor
source_tensor = torch.randn(4, 5)

# Perform scatter operation
output_tensor = torch.scatter(input_tensor.clone(), 1, index_tensor.unsqueeze(-1).expand(-1, 5), source_tensor)

print(output_tensor)