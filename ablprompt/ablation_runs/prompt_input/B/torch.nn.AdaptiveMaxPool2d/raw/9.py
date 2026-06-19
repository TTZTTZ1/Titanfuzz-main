import torch
import torch.nn as nn

# Create a random input tensor
input_tensor = torch.randn(1, 3, 20, 30)

# Define AdaptiveMaxPool2d layer with dynamic output size
output_height = torch.randint(1, 10, (1,))
output_width = torch.randint(1, 10, (1,))
adaptive_max_pool = nn.AdaptiveMaxPool2d((output_height.item(), output_width.item()))

# Apply the layer to the input tensor
output_tensor = adaptive_max_pool(input_tensor)

print("Input Shape:", input_tensor.shape)
print("Output Shape:", output_tensor.shape)