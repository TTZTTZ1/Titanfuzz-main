import torch

input_tensor = torch.randn(1, 3, 4, 5)
padding_tuple = (1, 2, 3, 4, 5, 6)

reflection_pad = torch.nn.ReflectionPad3d(padding=padding_tuple)
output_tensor = reflection_pad(input_tensor)