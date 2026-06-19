import torch
from torch import nn

# Define a simple 3D Convolutional Neural Network
class SimpleConv3dNet(nn.Module):
    def __init__(self):
        super(SimpleConv3dNet, self).__init__()
        self.conv3d = nn.Conv3d(in_channels=16, out_channels=32, kernel_size=(3, 3, 3), stride=(1, 1, 1), padding=(1, 1, 1))

    def forward(self, x):
        return self.conv3d(x)

# Create a dummy input tensor
input_tensor = torch.randn(1, 16, 32, 32, 32)

# Initialize the network and perform a forward pass
net = SimpleConv3dNet()
output = net(input_tensor)
print(output.shape)