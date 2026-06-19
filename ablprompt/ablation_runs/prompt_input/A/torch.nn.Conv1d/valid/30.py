import torch

# Define input tensor and convolution parameters
input_tensor = torch.randn(1, 3, 5)  # Batch size of 1, 3 input channels, sequence length of 5
weight = torch.randn(3, 1, 2)       # 3 output channels, 1 input channel, kernel size of 2
bias = torch.randn(3)               # 3 bias terms for each output channel

# Create a Conv1d layer
conv_layer = torch.nn.Conv1d(in_channels=3, out_channels=3, kernel_size=2)

# Apply the convolution operation
output_tensor = conv_layer(input_tensor)

print(output_tensor)