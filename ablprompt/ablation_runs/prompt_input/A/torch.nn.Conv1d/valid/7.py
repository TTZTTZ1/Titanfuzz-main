import torch
import torch.nn as nn

# Define a simple model using Conv1d
class SimpleConvModel(nn.Module):
    def __init__(self):
        super(SimpleConvModel, self).__init__()
        self.conv = nn.Conv1d(in_channels=3, out_channels=64, kernel_size=3, stride=1, padding=1)

    def forward(self, x):
        return self.conv(x)

# Create an instance of the model and a dummy input tensor
model = SimpleConvModel()
input_tensor = torch.randn(1, 3, 28)  # Batch size of 1, 3 channels, sequence length of 28

# Forward pass through the model
output = model(input_tensor)
print(output.shape)  # Expected output shape: [1, 64, 28]