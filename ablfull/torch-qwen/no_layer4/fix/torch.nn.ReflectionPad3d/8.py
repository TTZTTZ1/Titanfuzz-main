import torch
padding = ((1, 1), (1, 1), (1, 1))
result = torch.nn.ReflectionPad3d(padding)