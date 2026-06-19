
import torch
input_tensor = torch.randn(1, 1, 2, 4, 4)
padding = (1, 1, 1, 1, 1, 1)
result = torch.nn.ReflectionPad3d(padding)(input_tensor)
