import torch
import torch.nn as nn

# Define a simple model with MaxPool2d layer
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        self.fc = nn.Linear(64 * 16 * 16, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = self.pool(x)
        x = x.view(-1, 64 * 16 * 16)
        x = self.fc(x)
        return x

# Create a random input tensor
input_tensor = torch.randn(1, 3, 32, 32)

# Initialize the model and perform a forward pass
model = SimpleModel()
output = model(input_tensor)
print(output.shape)