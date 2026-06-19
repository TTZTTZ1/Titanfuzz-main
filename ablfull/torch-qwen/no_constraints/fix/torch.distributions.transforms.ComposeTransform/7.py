import torch
parts = [torch.nn.Identity()]
cache_size = 0
transform = torch.distributions.transforms.ComposeTransform(parts, cache_size)