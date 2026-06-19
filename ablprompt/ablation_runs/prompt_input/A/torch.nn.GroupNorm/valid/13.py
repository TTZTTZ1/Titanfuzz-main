import torch
import torch.nn as nn

# Define a simple model using GroupNorm
class SimpleModel(nn.Module):
    def __init__(self, num_features, num_groups):
        super(SimpleModel, self).__init__()
        self.conv = nn.Conv2d(1, 32, kernel_size=3, padding=1)
        self.group_norm = nn.GroupNorm(num_groups, num_features)

    def forward(self, x):
        x = self.conv(x)
        x = self.group_norm(x)
        return x

# Example usage
model = SimpleModel(num_features=32, num_groups=4)
input_tensor = torch.randn(1, 1, 32, 32)  # Batch size of 1, 1 channel, 32x32 image
output = model(input_tensor)
print(output.shape)  # Should be [1, 32, 32, 32]