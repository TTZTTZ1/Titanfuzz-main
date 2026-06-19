import torch
import torch.nn as nn

# Define a simple model using Conv1d
class SimpleConv1dModel(nn.Module):
    def __init__(self):
        super(SimpleConv1dModel, self).__init__()
        self.conv = nn.Conv1d(in_channels=3, out_channels=64, kernel_size=5)

    def forward(self, x):
        return self.conv(x)

# Create an instance of the model and input tensor
model = SimpleConv1dModel()
input_tensor = torch.randn(1, 3, 20)  # Batch size 1, 3 channels, sequence length 20

# Forward pass through the model
output = model(input_tensor)
print(output.shape)  # Expected output shape: [1, 64, 16]