import torch

# Define input tensor and convolutional layer parameters
input_tensor = torch.randn(1, 3, 5)  # Batch size=1, in_channels=3, sequence length=5
conv_layer = torch.nn.Conv1d(in_channels=3, out_channels=6, kernel_size=2)

# Perform the convolution operation
output_tensor = conv_layer(input_tensor)

print(output_tensor)