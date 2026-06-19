import torch

# Task 2: Generate input data
input_data = torch.randn(1, 3, 4, 5, 6)

# Task 3: Call the API
padding = (1, 2, 3, 4, 5, 6)
output = torch.nn.ReflectionPad3d(padding)(input_data)