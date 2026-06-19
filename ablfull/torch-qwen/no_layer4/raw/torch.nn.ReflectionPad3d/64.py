import torch

# Prepare valid input data
padding = ((1, 1), (1, 1), (1, 1))

# Call the API
result = torch.nn.ReflectionPad3d(padding)