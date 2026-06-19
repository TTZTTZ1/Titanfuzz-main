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
model = SimpleModel(num_features=16, num_groups=4)
input_tensor = torch.randn(32, 16, 7, 7)  # Batch size of 32, 16 features, and a spatial dimension of 7x7
output_tensor = model(input_tensor)
print(output_tensor.shape)  # Should print: torch.Size([32, 16, 7, 7])