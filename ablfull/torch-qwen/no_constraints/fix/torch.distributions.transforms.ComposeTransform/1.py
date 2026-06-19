import torch
parts = [torch.distributions.transforms.ExpTransform(), torch.distributions.transforms.SigmoidTransform()]
cache_size = 0
transform = torch.distributions.transforms.ComposeTransform(parts, cache_size)