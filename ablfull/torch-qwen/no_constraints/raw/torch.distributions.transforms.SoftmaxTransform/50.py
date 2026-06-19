import torch
from torch.distributions.transforms import SoftmaxTransform

# Generate input data
cache_size = 10

# Call the API
transform = SoftmaxTransform(cache_size=cache_size)