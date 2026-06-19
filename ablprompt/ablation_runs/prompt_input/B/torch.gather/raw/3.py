import torch

# Create a sample input tensor
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])

# Create an index tensor
index_tensor = torch.tensor([[0, 2, 1], [2, 0, 1]])

# Use torch.gather to gather elements from input_tensor based on index_tensor along dimension 1
output_tensor = torch.gather(input_tensor, 1, index_tensor.unsqueeze(-1).expand(-1, -1, input_tensor.shape[2]))

print(output_tensor)