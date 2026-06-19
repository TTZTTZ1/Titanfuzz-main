import torch
from torch.distributions.transforms import ComposeTransform, PowerTransform
parts = [PowerTransform(exponent=0.5)]
cache_size = 0
transform = ComposeTransform(parts, cache_size)