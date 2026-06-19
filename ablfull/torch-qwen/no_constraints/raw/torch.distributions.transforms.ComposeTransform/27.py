import torch
from torch.distributions import transforms

# Task 2: Generate input data
parts = [transforms.Sigmoid(), transforms.Exp()]
cache_size = 0

# Task 3: Call the API
transform = transforms.ComposeTransform(parts, cache_size)