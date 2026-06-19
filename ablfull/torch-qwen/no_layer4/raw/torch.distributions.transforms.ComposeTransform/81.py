import torch
from torch.distributions import transforms

# Prepare valid input data
parts = [transforms.ExpTransform(), transforms.SigmoidTransform()]
cache_size = 0

# Call the API
transform = transforms.ComposeTransform(parts, cache_size)