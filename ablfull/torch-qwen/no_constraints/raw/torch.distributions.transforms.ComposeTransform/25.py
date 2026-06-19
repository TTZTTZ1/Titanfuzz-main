import torch
from torch.distributions.transforms import ComposeTransform, PowerTransform

# Task 2: Generate input data
parts = [PowerTransform(2.0), PowerTransform(0.5)]

# Task 3: Call the API
transform = ComposeTransform(parts)