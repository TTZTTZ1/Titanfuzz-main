import torch
import torch.nn as nn

# Define a simple model using Conv2d
class SimpleConvModel(nn.Module):
    def __init__(self):
        super(SimpleConvModel, self).__init__()
        self.conv = nn.Conv2d(in_channels=1, out_channels=3, kernel_size=3, stride=1, padding=1)

    def forward(self, x):
        return self.conv(x)

# Create an instance of the model and input tensor
model = SimpleConvModel()
input_tensor = torch.randn(1, 1, 5, 5)  # Batch size 1, 1 channel, 5x5 image

# Perform the convolution
output = model(input_tensor)
print(output.shape)  # Expected output shape: [1, 3, 5, 5]