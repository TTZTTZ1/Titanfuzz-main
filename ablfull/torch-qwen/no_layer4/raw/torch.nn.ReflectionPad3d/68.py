import torch

# Task 2: Generate input data
input_tensor = torch.randn(1, 3, 4, 4, 4)

# Task 3: Call the API
pad_layer = torch.nn.ReflectionPad3d((1, 1, 1, 1, 1, 1))
padded_tensor = pad_layer(input_tensor)