import torch

# Prepare valid input data
cache_size = 0

# Call the target API
transform = torch.distributions.transforms.SoftmaxTransform(cache_size=cache_size)