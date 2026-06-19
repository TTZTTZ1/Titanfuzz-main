import torch

# Generate input data
cache_size = 1  # Example valid value within the specified constraint

# Call the API
transform = torch.distributions.transforms.SoftmaxTransform(cache_size=cache_size)