import torch

# Prepare input data
parts = [torch.nn.Identity()]
cache_size = 0

# Call the API
transform = torch.distributions.transforms.ComposeTransform(parts, cache_size)