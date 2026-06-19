import torch

# Generate a 3x3 tensor of random floats between -1 and 1
input_tensor = torch.randn(3, 3)

# Ensure the input tensor is of type float
input_tensor = input_tensor.float()

# Call the torch.slogdet function
result = torch.slogdet(input_tensor)