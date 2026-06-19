import torch

# Define the input tensor
input_tensor = torch.randn(1, 3, 4, 5, 6)

# Create a Conv3d layer
conv_layer = torch.nn.Conv3d(in_channels=3, out_channels=8, kernel_size=(3, 3, 3), stride=(1, 1, 1), padding=(1, 1, 1))

# Apply the convolution
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)