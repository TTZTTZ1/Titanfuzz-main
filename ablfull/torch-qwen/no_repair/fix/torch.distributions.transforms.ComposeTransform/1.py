
import torch
parts = []
cache_size = 0
transform = torch.distributions.transforms.ComposeTransform(parts, cache_size)
