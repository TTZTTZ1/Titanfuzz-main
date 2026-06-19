import torch

# Prepare input data
padding = (1, 2, 3, 4, 5, 6)

# Call the API
result = torch.nn.ReflectionPad3d(padding)