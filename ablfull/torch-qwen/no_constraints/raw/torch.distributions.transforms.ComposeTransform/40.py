import torch
from torch.distributions.transforms import ComposeTransform, Lambda

# Task 2: Generate input data
parts = [Lambda(lambda x: x * 2), Lambda(lambda x: x + 1)]
cache_size = 5

# Task 3: Call the API
transform = ComposeTransform(parts, cache_size)