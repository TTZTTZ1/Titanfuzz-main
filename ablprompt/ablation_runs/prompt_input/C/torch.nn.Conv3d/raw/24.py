import torch

# Define the input tensor
input_tensor = torch.randn(1, 16, 32, 32, 32)

# Create a Conv3d layer
conv_layer = torch.nn.Conv3d(in_channels=16, out_channels=8, kernel_size=(3, 3, 3), stride=(1, 1, 1), padding=(1, 1, 1), bias=True)

# Apply the convolutional layer
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)