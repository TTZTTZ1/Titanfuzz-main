import torch
from torch.distributions import transforms
parts = [transforms.ExpTransform(), transforms.SigmoidTransform()]
cache_size = 0
transform = transforms.ComposeTransform(parts, cache_size)