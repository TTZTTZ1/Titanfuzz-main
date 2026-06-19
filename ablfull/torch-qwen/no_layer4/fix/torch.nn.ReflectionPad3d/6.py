import torch
padding = (1, 2, 3, 4, 5, 6)
input_tensor = torch.randn(1, 1, 10, 10, 10)
torch.nn.ReflectionPad3d(padding)(input_tensor)