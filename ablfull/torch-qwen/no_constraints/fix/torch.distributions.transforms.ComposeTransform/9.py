import torch
from torch.distributions.transforms import ComposeTransform, PowerTransform
parts = [PowerTransform(2.0), PowerTransform(0.5)]
transform = ComposeTransform(parts)