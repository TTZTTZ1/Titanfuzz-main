import torch
from torch.nn import ReflectionPad3d
input_tensor = torch.randn(1, 1, 4, 5, 6)
padding = (1, 1, 1, 1, 1, 1)
reflection_pad = ReflectionPad3d(padding)
output_tensor = reflection_pad(input_tensor)