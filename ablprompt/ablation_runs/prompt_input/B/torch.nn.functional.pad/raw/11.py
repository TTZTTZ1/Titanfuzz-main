import torch
import torch.nn.functional as F

# Create a random tensor
input_tensor = torch.randn(3, 4, 5)

# Define padding
pad = (1, 1, 2, 2, 3, 3)

# Apply padding using 'constant' mode with a specific value
output_tensor = F.pad(input_tensor, pad, mode='constant', value=0.5)

print(output_tensor.shape)  # Output should be (3, 8, 10)