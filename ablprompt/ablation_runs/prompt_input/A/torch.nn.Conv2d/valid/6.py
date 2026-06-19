import torch
import torch.nn as nn

# Define a simple model using Conv2d
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv = nn.Conv2d(in_channels=1, out_channels=3, kernel_size=3, stride=1, padding=1)

    def forward(self, x):
        return self.conv(x)

# Create an instance of the model and input tensor
model = SimpleModel()
input_tensor = torch.randn(1, 1, 5, 5)  # Batch size 1, 1 channel, 5x5 image

# Perform the forward pass
output = model(input_tensor)
print(output.shape)