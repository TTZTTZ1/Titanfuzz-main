import torch

# Prepare valid input data
cache_size = 5

# Call the API
transform = torch.distributions.transforms.SoftmaxTransform(cache_size=cache_size)