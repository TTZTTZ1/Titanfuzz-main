import torch

# Task 2: Generate input data
parts = [torch.distributions.transforms.ExpTransform(), torch.distributions.transforms.SigmoidTransform()]
cache_size = 5

# Task 3: Call the API
transform = torch.distributions.transforms.ComposeTransform(parts, cache_size)