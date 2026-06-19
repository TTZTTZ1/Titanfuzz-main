
import torch
padding = ((0, 1), (2, 3), (4, 5))
output = torch.nn.ReflectionPad3d(padding)
