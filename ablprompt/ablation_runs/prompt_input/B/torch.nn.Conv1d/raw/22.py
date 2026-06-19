import torch
from torch import nn

# Define a simple model using Conv1d
class SimpleConvNet(nn.Module):
    def __init__(self):
        super(SimpleConvNet, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=16, out_channels=32, kernel_size=3, stride=2, padding=1, groups=8, bias=False, padding_mode='replicate')
    
    def forward(self, x):
        return self.conv1(x)

# Create an instance of the model and some random input
model = SimpleConvNet()
input_tensor = torch.randn(10, 16, 50)  # Batch of 10, 16 channels, length 50
output = model(input_tensor)

print(output.shape)  # Expected output shape: (10, 32, 24)