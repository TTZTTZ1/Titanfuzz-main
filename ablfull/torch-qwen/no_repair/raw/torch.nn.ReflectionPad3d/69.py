import torch

# Task 2: Generate input data
input_tensor = torch.randn(1, 1, 2, 4, 4)
padding = (1, 1, 1, 1, 1, 1)

# Task 3: Call the API
result = torch.nn.ReflectionPad3d(padding)(input_tensor)