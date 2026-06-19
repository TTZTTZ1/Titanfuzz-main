import torch
from torch import nn

# Define a simple model using Conv2d
class SimpleConvModel(nn.Module):
    def __init__(self):
        super(SimpleConvModel, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3, stride=1, padding=1)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        self.fc = nn.Linear(in_features=64 * 16 * 16, out_features=10)

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool(x)
        x = x.view(-1, 64 * 16 * 16)
        x = self.fc(x)
        return x

# Create an instance of the model
model = SimpleConvModel()

# Example input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Forward pass
output = model(input_tensor)
print(output.shape)