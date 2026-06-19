import torch

# Generate input data
parts = [torch.nn.Sigmoid(), torch.nn.Tanh()]
cache_size = 0

# Call the API
transform = torch.distributions.transforms.ComposeTransform(parts, cache_size)