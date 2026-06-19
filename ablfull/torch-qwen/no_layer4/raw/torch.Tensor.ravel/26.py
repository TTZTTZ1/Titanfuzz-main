import torch

# Generate input data
input_tensor = torch.randn(4, 5)

# Call the API
raveled_tensor = input_tensor.ravel()