import torch
import torch.nn as nn

# Define a simple model with Conv2d layer
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv_layer = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=(3, 3), stride=1, padding=1, bias=True)

    def forward(self, x):
        return self.conv_layer(x)

# Create an instance of the model and a random input tensor
model = SimpleCNN()
input_tensor = torch.randn(1, 3, 32, 32)

# Forward pass through the model
output = model(input_tensor)
print(output.shape)