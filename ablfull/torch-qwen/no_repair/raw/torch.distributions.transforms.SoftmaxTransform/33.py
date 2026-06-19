import torch

# Prepare valid input data
cache_size = 1  # Ensure it is within the specified range [0, 1]

# Call the API
transform = torch.distributions.transforms.SoftmaxTransform(cache_size=cache_size)