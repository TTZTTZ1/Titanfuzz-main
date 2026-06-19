
import torch
cache_size = 1
transform = torch.distributions.transforms.SoftmaxTransform(cache_size=cache_size)
