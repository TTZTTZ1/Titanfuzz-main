import torch

# Generate input data
input_tensor = torch.randn(4, 5)
dim0 = 0
dim1 = 1

# Call the API
transposed_tensor = torch.transpose(input_tensor, dim0, dim1)
print(transposed_tensor)