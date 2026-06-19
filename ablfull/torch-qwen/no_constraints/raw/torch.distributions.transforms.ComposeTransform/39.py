import torch
from torch.distributions.transforms import ComposeTransform, LogitTransform, PowerTransform

# Prepare input data
parts = [LogitTransform(), PowerTransform(2)]
cache_size = 0

# Call the API
transform = ComposeTransform(parts, cache_size)