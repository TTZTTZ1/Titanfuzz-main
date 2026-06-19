import torch
import torch.nn as nn

# Define a simple model with GroupNorm
class SimpleModel(nn.Module):
    def __init__(self, num_channels=64, num_groups=8):
        super(SimpleModel, self).__init__()
        self.conv1 = nn.Conv2d(num_channels, num_channels, kernel_size=3, padding=1)
        self.group_norm = nn.GroupNorm(num_groups, num_channels)
        self.relu = nn.ReLU()
        self.fc = nn.Linear(num_channels * 7 * 7, 10)

    def forward(self, x):
        x = self.conv1(x)
        x = self.group_norm(x)
        x = self.relu(x)
        x = x.view(x.size(0), -1)
        x = self.fc(x)
        return x

# Example usage
model = SimpleModel()
input_tensor = torch.randn(1, 64, 28, 28)
output = model(input_tensor)
print(output.shape)