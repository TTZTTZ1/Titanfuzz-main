import torch
parts = [torch.nn.functional.relu]
transform = torch.distributions.transforms.ComposeTransform(parts)