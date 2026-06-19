import torch
from torch.nn.functional import pad

# Create a sample tensor
input_tensor = torch.randn(2, 3, 4)

# Define the padding
pad_values = (1, 1, 2, 2, 3, 3)  # Padding for each dimension: (left, right, top, bottom, front, back)

# Apply padding using the 'constant' mode
output_tensor = pad(input_tensor, pad_values, mode='constant', value=0)

print(output_tensor.shape)  # Output should be (6, 7, 8)