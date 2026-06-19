import torch

# Create a random input tensor with shape (1, 3, 4, 5, 6)
input_tensor = torch.randn(1, 3, 4, 5, 6)

# Define the Conv3d layer with specific parameters
conv_layer = torch.nn.Conv3d(in_channels=3, out_channels=8, kernel_size=(2, 3, 4), stride=(1, 2, 2), padding=(1, 1, 1), dilation=(1, 1, 1), groups=1, bias=True, padding_mode='zeros')

# Apply the convolutional layer to the input tensor
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)  # Output should be (1, 8, 3, 3, 4)