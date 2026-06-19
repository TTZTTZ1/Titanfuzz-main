import torch

# Prepare valid input data
cache_size = 0  # Valid value within the specified range

# Call the API
transform = torch.distributions.transforms.SoftmaxTransform(cache_size=cache_size)