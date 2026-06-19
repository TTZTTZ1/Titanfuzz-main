import torch

# Create a random 5D tensor
input_tensor = torch.randn(1, 3, 4, 4, 4)

# Define the MaxPool3d layer
maxpool = torch.nn.MaxPool3d(kernel_size=2, stride=2, padding=0)

# Apply the MaxPool3d layer to the input tensor
output_tensor = maxpool(input_tensor)

print(output_tensor)