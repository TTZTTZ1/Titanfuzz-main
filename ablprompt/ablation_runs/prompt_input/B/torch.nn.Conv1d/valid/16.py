import torch
import torch.nn as nn

# Define a simple model using Conv1d
class SimpleConvModel(nn.Module):
    def __init__(self):
        super(SimpleConvModel, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=16, out_channels=33, kernel_size=3, stride=2, padding=1)
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool1d(kernel_size=2)

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool(x)
        return x

# Create an instance of the model and a dummy input tensor
model = SimpleConvModel()
input_tensor = torch.randn(20, 16, 50)

# Forward pass through the model
output = model(input_tensor)
print(output.shape)  # Expected output shape: (20, 33, 24)