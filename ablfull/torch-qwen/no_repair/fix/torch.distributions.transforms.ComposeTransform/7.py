
import torch
parts = []
cache_size = (1 if torch.randint(0, 2, (1,)).item() else 0)
transform = torch.distributions.transforms.ComposeTransform(parts, cache_size)
