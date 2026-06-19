import torch
import torch.nn as nn

# Define a simple model using LayerNorm
class SimpleModel(nn.Module):
    def __init__(self, input_size, normalized_shape):
        super(SimpleModel, self).__init__()
        self.layer_norm = nn.LayerNorm(normalized_shape)

    def forward(self, x):
        return self.layer_norm(x)

# Example usage
input_tensor = torch.randn(10, 20)  # Batch size of 10, feature dimension of 20
model = SimpleModel(input_size=20, normalized_shape=[20])
output_tensor = model(input_tensor)
print(output_tensor.shape)  # Should be [10, 20]