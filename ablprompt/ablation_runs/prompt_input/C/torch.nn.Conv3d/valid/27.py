import torch
from torch import nn

# Define a simple 3D Convolutional Neural Network
class SimpleConv3dNet(nn.Module):
    def __init__(self):
        super(SimpleConv3dNet, self).__init__()
        # Input dimensions: N x 1 x 64 x 64 x 64
        self.conv1 = nn.Conv3d(in_channels=1, out_channels=32, kernel_size=(3, 3, 3), stride=(1, 1, 1), padding=(1, 1, 1))
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool3d(kernel_size=(2, 2, 2), stride=(2, 2, 2))

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool(x)
        return x

# Create an instance of the network and a dummy input tensor
net = SimpleConv3dNet()
input_tensor = torch.randn(1, 1, 64, 64, 64)

# Forward pass through the network
output_tensor = net(input_tensor)
print(output_tensor.shape)  # Expected output shape: torch.Size([1, 32, 32, 32, 32])