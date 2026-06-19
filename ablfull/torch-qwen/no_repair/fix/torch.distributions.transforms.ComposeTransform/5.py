
import torch
from torch.distributions.transforms import ComposeTransform, ExpTransform
parts = [ExpTransform()]
cache_size = 0
transform = ComposeTransform(parts, cache_size)
