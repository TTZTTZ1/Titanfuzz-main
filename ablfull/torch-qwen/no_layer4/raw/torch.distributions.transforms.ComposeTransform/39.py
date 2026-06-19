import torch

# Generate input data
parts = [torch.distributions.transforms.Exp()]
cache_size = 0

# Call the API
transform = torch.distributions.transforms.ComposeTransform(parts, cache_size)