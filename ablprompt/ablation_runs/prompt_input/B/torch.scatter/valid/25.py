import torch

# Create a tensor to be scattered
input_tensor = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)

# Create an index tensor specifying where to scatter
index_tensor = torch.tensor([[0, 1], [1, 0]], dtype=torch.long)

# Create a source tensor containing the values to scatter
source_tensor = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)

# Perform the scatter operation
output_tensor = torch.scatter(input_tensor, 1, index_tensor, source_tensor)

print(output_tensor)