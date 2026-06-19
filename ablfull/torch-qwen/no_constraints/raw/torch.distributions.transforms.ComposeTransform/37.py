import torch

# Task 2: Generate input data
parts = [torch.distributions.transforms.ExpTransform(), torch.distributions.transforms.SigmoidTransform()]

# Task 3: Call the API
ComposeTransform = torch.distributions.transforms.ComposeTransform(parts)