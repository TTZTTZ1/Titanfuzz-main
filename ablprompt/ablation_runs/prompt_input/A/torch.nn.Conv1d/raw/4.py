import torch
import torch.nn as nn

# Define a simple model using Conv1d
class SimpleConvModel(nn.Module):
    def __init__(self):
        super(SimpleConvModel, self).__init__()
        # Create a 1D convolutional layer
        self.conv = nn.Conv1d(in_channels=3, out_channels=64, kernel_size=5, stride=1, padding=2)

    def forward(self, x):
        return self.conv(x)

# Example usage
model = SimpleConvModel()
input_tensor = torch.randn(1, 3, 10)  # Batch size of 1, 3 input channels, sequence length of 10
output = model(input_tensor)
print(output.shape)  # Should print: torch.Size([1, 64, 10])