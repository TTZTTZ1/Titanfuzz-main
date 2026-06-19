import torch

input_tensor = torch.randn(1, 3, 4, 5)
padding = (1, 2, 3, 4, 5, 6)
result = torch.nn.ReflectionPad3d(padding)(input_tensor)