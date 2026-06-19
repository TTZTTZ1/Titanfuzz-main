import torch

# Create a sample input tensor
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])

# Create an index tensor specifying the positions where values will be scattered
index_tensor = torch.tensor([[0, 1], [1, 0]])

# Create a source tensor containing the values to scatter
source_tensor = torch.tensor([[9.0, 8.0], [7.0, 6.0]])

# Perform the scatter operation along dimension 1
result_tensor = torch.scatter(input_tensor, 1, index_tensor, source_tensor)

print(result_tensor)