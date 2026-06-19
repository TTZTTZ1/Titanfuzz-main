import torch
padding = (1, 2, 3, 4, 5, 6)
reflection_pad = torch.nn.ReflectionPad3d(padding)