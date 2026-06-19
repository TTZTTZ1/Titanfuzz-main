import torch

# Prepare valid input data
parts = [torch.distributions.transforms.Exp(), torch.distributions.transforms.Sigmoid()]
cache_size = 0

# Call the API
transform = torch.distributions.transforms.ComposeTransform(parts, cache_size)