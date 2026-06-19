import torch

transform = torch.distributions.transforms.ComposeTransform([torch.distributions.transforms.Exp()])
result = transform(torch.tensor(1.0))