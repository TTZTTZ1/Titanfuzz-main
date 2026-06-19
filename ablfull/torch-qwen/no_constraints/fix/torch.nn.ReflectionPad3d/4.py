import torch
input_tensor = torch.randn(1, 1, 2, 2, 2)
padding = (1, 1, 1, 1, 1, 1)
output_tensor = torch.nn.ReflectionPad3d(padding)(input_tensor)