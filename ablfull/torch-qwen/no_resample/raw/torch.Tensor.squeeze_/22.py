import torch

# Prepare input data
input_tensor = torch.randn(1, 1, 2, 3)

# Call the API
result = input_tensor.squeeze_(dim=0)