import torch

transform = torch.distributions.transforms.IdentityTransform()
transforms = [transform]
composed_transform = torch.distributions.transforms.ComposeTransform(transforms)