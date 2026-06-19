import torch

# Task 2: Generate input data
input_data = torch.randn(1, 1, 4, 4, 4)

# Task 3: Call the API
output = torch.nn.ReflectionPad3d((1, 2, 3, 4, 5, 6))(input_data)