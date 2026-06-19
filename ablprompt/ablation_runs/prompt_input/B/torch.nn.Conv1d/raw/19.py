import torch
import torch.nn as nn

# Define a simple model using Conv1d
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=16, out_channels=33, kernel_size=3, stride=2, padding=1, groups=8, bias=True, padding_mode='reflect')
        self.relu = nn.ReLU()
        self.pool = nn.MaxPool1d(kernel_size=2, stride=2)

    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool(x)
        return x

# Create a dummy input tensor
input_tensor = torch.randn(10, 16, 50)

# Initialize the model
model = SimpleModel()

# Forward pass
output_tensor = model(input_tensor)
print(output_tensor.shape)