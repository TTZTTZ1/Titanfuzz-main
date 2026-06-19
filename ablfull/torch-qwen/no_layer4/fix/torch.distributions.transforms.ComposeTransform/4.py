import torch
parts = [torch.nn.Sigmoid(), torch.nn.Tanh()]
cache_size = 0
transform = torch.distributions.transforms.ComposeTransform(parts, cache_size)