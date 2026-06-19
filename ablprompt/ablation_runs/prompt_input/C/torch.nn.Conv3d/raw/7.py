import torch

# Create a random input tensor with shape (batch_size, in_channels, depth, height, width)
input_tensor = torch.randn(1, 16, 32, 32, 32)

# Define the Conv3d layer
conv_layer = torch.nn.Conv3d(in_channels=16, out_channels=8, kernel_size=(3, 3, 3), stride=(1, 1, 1), padding=(1, 1, 1), padding_mode='zeros')

# Apply the convolutional layer to the input tensor
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)