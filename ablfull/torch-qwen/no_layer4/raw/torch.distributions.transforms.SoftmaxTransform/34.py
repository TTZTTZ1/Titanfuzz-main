import torch

# Generate input data
cache_size = 1

# Call the API
transform = torch.distributions.transforms.SoftmaxTransform(cache_size=cache_size)