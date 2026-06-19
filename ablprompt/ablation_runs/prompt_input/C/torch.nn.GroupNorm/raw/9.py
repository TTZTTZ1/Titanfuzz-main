import torch
import torch.nn as nn

# Define a model with GroupNorm
class GroupNormModel(nn.Module):
    def __init__(self, num_channels):
        super(GroupNormModel, self).__init__()
        self.group_norm = nn.GroupNorm(num_groups=3, num_channels=num_channels)

    def forward(self, x):
        return self.group_norm(x)

# Example usage
model = GroupNormModel(num_channels=6)
input_tensor = torch.randn(1, 6, 4, 4)  # Batch size 1, 6 channels, 4x4 spatial dimensions
output_tensor = model(input_tensor)
print(output_tensor.shape)  # Should be the same as input shape: torch.Size([1, 6, 4, 4])