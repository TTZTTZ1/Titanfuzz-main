import torch
parts = [torch.distributions.transforms.ExpTransform(), torch.distributions.transforms.SigmoidTransform()]
ComposeTransform = torch.distributions.transforms.ComposeTransform(parts)