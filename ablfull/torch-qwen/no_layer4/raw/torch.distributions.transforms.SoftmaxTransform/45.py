import torch

# Prepare input data
cache_size = 0

# Call the API
transform = torch.distributions.transforms.SoftmaxTransform(cache_size=cache_size)