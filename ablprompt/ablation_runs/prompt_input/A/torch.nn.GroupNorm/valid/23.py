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
if __name__ == "__main__":
    # Create an instance of the model
    model = SimpleModel(num_features=64, num_groups=8)
    
    # Create a dummy input tensor
    input_tensor = torch.randn(10, 64, 32, 32)  # Batch size: 10, Features: 64, Height: 32, Width: 32
    
    # Forward pass through the model
    output_tensor = model(input_tensor)
    
    print(output_tensor.shape)  # Should be the same shape as input_tensor