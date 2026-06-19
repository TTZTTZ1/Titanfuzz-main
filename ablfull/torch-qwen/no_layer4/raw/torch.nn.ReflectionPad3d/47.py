import torch

# Task 2: Generate input data
padding = (1, 2, 3, 4, 5, 6)

# Task 3: Call the API
reflection_pad = torch.nn.ReflectionPad3d(padding)