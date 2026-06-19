import torch

# Generate input data
input_tensor = torch.randn(1, 1, 2, 2)

# Call the API
result = input_tensor.squeeze_(dim=0)