import torch
padding = (1, 2, 3, 4, 5, 6)
pad_layer = torch.nn.ReflectionPad3d(padding)