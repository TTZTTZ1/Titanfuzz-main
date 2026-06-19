
import torch
parts = []
cache_size = 0
transform = torch.distributions.transforms.ComposeTransform(parts=parts, cache_size=cache_size)
