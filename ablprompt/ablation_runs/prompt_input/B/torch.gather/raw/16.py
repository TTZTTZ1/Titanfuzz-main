import torch

# Create a sample input tensor
input_tensor = torch.randn(3, 4)

# Create an index tensor
index_tensor = torch.LongTensor([[0, 2], [1, 3], [2, 1]])

# Use torch.gather to select elements
output_tensor = torch.gather(input_tensor, 1, index_tensor.unsqueeze(-1).expand(-1, -1, input_tensor.shape[2]))

print(output_tensor)