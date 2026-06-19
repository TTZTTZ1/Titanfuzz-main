import torch

# Prepare valid input data
cache_size = 0  # Must be an integer within the range [0, 1]

# Call the API
transform = torch.distributions.transforms.SoftmaxTransform(cache_size=cache_size)