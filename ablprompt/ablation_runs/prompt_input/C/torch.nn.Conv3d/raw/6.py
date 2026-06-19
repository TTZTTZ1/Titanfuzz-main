import torch

# Define input tensor
input_tensor = torch.randn(1, 3, 5, 5, 5)

# Create Conv3d layer
conv_layer = torch.nn.Conv3d(in_channels=3, out_channels=64, kernel_size=(3, 3, 3), stride=(1, 1, 1), padding=(1, 1, 1))

# Apply convolution
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)