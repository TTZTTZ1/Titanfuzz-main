import torch
import torch.nn as nn

# Define a simple model with BatchNorm2d
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv1 = nn.Conv2d(3, 64, kernel_size=3, stride=1, padding=1)
        self.bn1 = nn.BatchNorm2d(64)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)

    def forward(self, x):
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu(x)
        x = self.pool(x)
        return x

# Create an instance of the model and move it to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = SimpleModel().to(device)

# Generate some random input data
input_data = torch.randn(1, 3, 32, 32).to(device)

# Forward pass through the model
output = model(input_data)
print(output.shape)