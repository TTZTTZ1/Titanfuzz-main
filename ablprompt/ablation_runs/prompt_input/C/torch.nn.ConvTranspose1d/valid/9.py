import torch
import torch.nn as nn

# Define a simple model using ConvTranspose1d
class TransposeConvModel(nn.Module):
    def __init__(self):
        super(TransposeConvModel, self).__init__()
        self.conv_transpose = nn.ConvTranspose1d(in_channels=16, out_channels=8, kernel_size=4, stride=2, padding=1)

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model
model = TransposeConvModel()

# Example input tensor
input_tensor = torch.randn(1, 16, 32)  # Batch size 1, 16 input channels, sequence length 32

# Forward pass through the model
output_tensor = model(input_tensor)

print(output_tensor.shape)  # Expected output shape: torch.Size([1, 8, 65])