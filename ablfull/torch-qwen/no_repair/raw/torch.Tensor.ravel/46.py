import torch

# Generate input data
data = torch.randn(4, 5)

# Call the API
raveled_data = data.ravel()