import torch
import torch.nn as nn

# Define a simple model using Conv1d
class SimpleConvModel(nn.Module):
    def __init__(self):
        super(SimpleConvModel, self).__init__()
        # Create a 1D convolutional layer
        self.conv1 = nn.Conv1d(in_channels=3, out_channels=64, kernel_size=3, stride=1, padding=1)

    def forward(self, x):
        # Pass input through the convolutional layer
        x = self.conv1(x)
        return x

# Example usage
model = SimpleConvModel()
input_tensor = torch.randn(1, 3, 28)  # Batch size of 1, 3 channels, sequence length of 28
output = model(input_tensor)
print(output.shape)  # Should print: torch.Size([1, 64, 28])