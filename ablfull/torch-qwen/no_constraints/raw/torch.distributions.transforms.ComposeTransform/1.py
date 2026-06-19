import torch

# Task 2: Generate input data
parts = [torch.distributions.transforms.Exp(), torch.distributions.transforms.Sigmoid()]

# Task 3: Call the API
transform = torch.distributions.transforms.ComposeTransform(parts)