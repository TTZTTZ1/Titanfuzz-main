import torch
import torch.nn as nn

# Define a random input tensor
input_tensor = torch.randn(1, 3, 10, 12)

# Create an AdaptiveMaxPool2d layer with specified output size
pool = nn.AdaptiveMaxPool2d((5, 7))

# Apply the pooling operation
output_tensor = pool(input_tensor)

print("Input Shape:", input_tensor.shape)
print("Output Shape:", output_tensor.shape)