import torch

padding = (0, 1, 2, 3, 4, 5)
input_tensor = torch.randn(1, 1, 2, 2, 2)
output_tensor = torch.nn.ReflectionPad3d(padding)(input_tensor)