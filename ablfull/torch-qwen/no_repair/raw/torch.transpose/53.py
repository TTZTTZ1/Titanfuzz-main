import torch

# Create a non-sparse tensor
input_tensor = torch.tensor([[1.0, 2.0], [3.0, 4.0]])

# Valid dimensions for transpose
dim0 = 0
dim1 = 1

# Call torch.transpose
result = torch.transpose(input_tensor, dim0, dim1)