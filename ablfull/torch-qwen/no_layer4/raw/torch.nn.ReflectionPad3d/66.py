import torch

# Generate input data
input_tensor = torch.randn(1, 3, 4, 5, 6)
padding_value = (0, 0, 0, 1, 1, 1)

# Call the API
output_tensor = torch.nn.functional.reflection_pad3d(input_tensor, padding_value)