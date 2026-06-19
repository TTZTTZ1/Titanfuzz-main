import torch

# Prepare valid input data
padding = (1, 2, 3)
input_tensor = torch.randn(1, 3, 4, 5, 6)

# Call the API
output_tensor = torch.nn.ReflectionPad3d(padding)(input_tensor)