import torch

# Prepare valid input data
parts = [torch.distributions.transforms.ExpTransform(), torch.distributions.transforms.SigmoidTransform()]
cache_size = 0

# Call the API
transform = torch.distributions.transforms.ComposeTransform(parts, cache_size)