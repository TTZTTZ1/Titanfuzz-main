import torch

# Generate input data
input_tensor = torch.randn(3, 4)

# Call the API
raveled_tensor = input_tensor.ravel()