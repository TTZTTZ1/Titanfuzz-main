import torch

# Create a 3x3 tensor
input_tensor = torch.randn(3, 3)

# Create an index tensor
index_tensor = torch.LongTensor([[0, 1, 2], [2, 0, 1], [1, 2, 0]])

# Gather elements along dimension 1
output_tensor = torch.gather(input_tensor, 1, index_tensor.unsqueeze(-1).expand(-1, -1, input_tensor.size(-1)))

print(output_tensor)