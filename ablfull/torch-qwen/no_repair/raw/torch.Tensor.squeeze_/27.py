import torch

# Prepare input data
tensor = torch.randn(1, 2, 1)

# Call the API
result = tensor.squeeze_(dim=0)