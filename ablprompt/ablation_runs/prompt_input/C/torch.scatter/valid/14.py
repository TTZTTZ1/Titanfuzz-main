import torch

# Create a sample input tensor
input_tensor = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)

# Create an index tensor
index_tensor = torch.tensor([[0, 1], [1, 0]], dtype=torch.long)

# Create a source tensor
source_tensor = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)

# Use torch.scatter to distribute values from source_tensor into input_tensor
output_tensor = torch.scatter(input_tensor, 1, index_tensor, source_tensor)

print(output_tensor)