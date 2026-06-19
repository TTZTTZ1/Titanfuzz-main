import torch

# Create a sample tensor
input_tensor = torch.tensor([[1, 2], [3, 4]])

# Define dimensions for transposition
dim0 = 0
dim1 = 1

# Call torch.transpose
result = torch.transpose(input_tensor, dim0, dim1)
print(result)