import torch

# Task 2: Generate input data
parts = [torch.distributions.transforms.Sigmoid(), torch.distributions.transforms.Exp()]
cache_size = 0

# Task 3: Call the API
transform = torch.distributions.transforms.ComposeTransform(parts, cache_size)