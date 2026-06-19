import torch
import torch.nn as nn

# Define a simple model using GroupNorm
class SimpleModel(nn.Module):
    def __init__(self, num_features, num_groups):
        super(SimpleModel, self).__init__()
        self.group_norm = nn.GroupNorm(num_groups, num_features)
    
    def forward(self, x):
        return self.group_norm(x)

# Example usage
model = SimpleModel(num_features=64, num_groups=8)
input_tensor = torch.randn(10, 64, 32, 32)  # Batch size of 10, 64 channels, 32x32 spatial dimensions
output_tensor = model(input_tensor)
print(output_tensor.shape)