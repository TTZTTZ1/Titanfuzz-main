import torch
import torch.nn as nn

# Define a simple model using Conv1d
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=1, out_channels=32, kernel_size=3, stride=1, padding=1)

    def forward(self, x):
        return self.conv1(x)

# Create an instance of the model and input tensor
model = SimpleModel()
input_tensor = torch.randn(1, 1, 10)  # Batch size 1, 1 channel, sequence length 10

# Perform a forward pass
output = model(input_tensor)
print(output.shape)  # Expected output shape: torch.Size([1, 32, 10])