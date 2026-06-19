import torch
import torch.nn as nn

# Define a model using GroupNorm
class GroupNormModel(nn.Module):
    def __init__(self):
        super(GroupNormModel, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding=1)
        self.group_norm = nn.GroupNorm(num_groups=32, num_channels=128)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.conv1(x)
        x = self.group_norm(x)
        x = self.relu(x)
        return x

# Create an instance of the model and a dummy input tensor
model = GroupNormModel()
input_tensor = torch.randn(1, 64, 32, 32)

# Forward pass through the model
output_tensor = model(input_tensor)
print(output_tensor.shape)