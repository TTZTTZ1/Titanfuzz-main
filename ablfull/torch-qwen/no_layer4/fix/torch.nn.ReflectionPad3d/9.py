import torch
input_tensor = torch.randn(1, 3, 4, 4, 4)
pad_layer = torch.nn.ReflectionPad3d((1, 1, 1, 1, 1, 1))
padded_tensor = pad_layer(input_tensor)