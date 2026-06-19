import torch

# Create a random input tensor
input_tensor = torch.randn(1, 16, 32, 32, 32)

# Define the Conv3d layer
conv_layer = torch.nn.Conv3d(in_channels=16, out_channels=32, kernel_size=(3, 3, 3), stride=(1, 1, 1), padding=(1, 1, 1))

# Apply the convolution
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)