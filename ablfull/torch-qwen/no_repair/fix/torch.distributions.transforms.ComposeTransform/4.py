
import torch
transform_parts = []
cache_size = 1
composed_transform = torch.distributions.transforms.ComposeTransform(transform_parts, cache_size)
