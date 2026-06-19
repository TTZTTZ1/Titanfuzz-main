import torch

# Create a random input tensor with shape (batch_size, in_channels, height, width)
input_tensor = torch.randn(1, 3, 64, 64)

# Define the Conv2d layer
conv_layer = torch.nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, stride=1, padding=1, bias=True)

# Apply the convolutional layer to the input tensor
output_tensor = conv_layer(input_tensor)

print(output_tensor.shape)  # Expected output shape: torch.Size([1, 16, 64, 64])