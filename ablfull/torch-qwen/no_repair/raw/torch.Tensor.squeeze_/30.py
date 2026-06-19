import torch

# Generate input data
tensor = torch.randn(1, 1, 3)

# Call the API
tensor.squeeze_(dim=0)