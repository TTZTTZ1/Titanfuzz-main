import torch
import torch.nn.functional as F

# Create a random tensor
input_tensor = torch.randn(4, 4)

# Define the padding
pad = (1, 1, 2, 2)

# Apply padding using 'constant' mode with a specific value
output_tensor = F.pad(input_tensor, pad, mode='constant', value=5.0)

print("Input Tensor:")
print(input_tensor)
print("Output Tensor after Padding:")
print(output_tensor)