import torch
parts = []
cache_size = 0
transforms = torch.distributions.transforms.ComposeTransform(parts, cache_size)