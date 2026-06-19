import torch
from torch import nn

# Define a simple 3D convolutional neural network
class SimpleConv3dNet(nn.Module):
    def __init__(self):
        super(SimpleConv3dNet, self).__init__()
        self.conv1 = nn.Conv3d(in_channels=1, out_channels=8, kernel_size=(3, 3, 3), stride=(1, 1, 1), padding=(1, 1, 1))
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool3d(kernel_size=(2, 2, 2))

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool(x)
        return x

# Create an instance of the network and a dummy input tensor
net = SimpleConv3dNet()
input_tensor = torch.randn(1, 1, 32, 32, 32)

# Perform a forward pass
output_tensor = net(input_tensor)

print(output_tensor.shape)