import torch
import torch.nn as nn

# Define a simple model using Conv1d
class SimpleConvNet(nn.Module):
    def __init__(self):
        super(SimpleConvNet, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=16, out_channels=33, kernel_size=3, stride=2, padding=1, bias=True)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool1d(kernel_size=2, stride=2)

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool(x)
        return x

# Create an instance of the model and run it on some dummy input
model = SimpleConvNet()
input_data = torch.randn(20, 16, 50)
output = model(input_data)
print(output.shape)  # Expected shape: (20, 33, 24)