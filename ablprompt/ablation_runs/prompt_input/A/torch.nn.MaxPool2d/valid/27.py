import torch
from torch.nn import MaxPool2d

# Create an input tensor
input_tensor = torch.randn(1, 3, 5, 5)

# Define the MaxPool2d layer
maxpool = MaxPool2d(kernel_size=2, stride=2, padding=0)

# Apply the MaxPool2d layer to the input tensor
output_tensor = maxpool(input_tensor)

print(output_tensor)