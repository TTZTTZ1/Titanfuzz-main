import torch
from torch.distributions import transforms

# Prepare valid input data
parts = [transforms.Exp(), transforms.Sigmoid()]
cache_size = 0

# Call the target API
compose_transform = transforms.ComposeTransform(parts, cache_size)