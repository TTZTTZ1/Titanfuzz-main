import torch

parts = [torch.distributions.transforms.Exp()]
cache_size = 0
transform = torch.distributions.transforms.ComposeTransform(parts, cache_size)