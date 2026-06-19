import torch
from torch import nn

# Define a simple model using ConvTranspose1d
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv_transpose = nn.ConvTranspose1d(in_channels=16, out_channels=8, kernel_size=3, stride=2, padding=1)

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model and input data
model = SimpleModel()
input_data = torch.randn(1, 16, 10)  # Batch size 1, 16 channels, sequence length 10

# Forward pass through the model
output = model(input_data)
print(output.shape)  # Expected output shape: [1, 8, 21]