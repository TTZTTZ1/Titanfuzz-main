import torch
cache_size = 0
transform = torch.distributions.transforms.SoftmaxTransform(cache_size=cache_size)