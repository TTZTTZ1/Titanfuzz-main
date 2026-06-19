import torch
import torch.nn as nn

# Define a simple model using Conv1d
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=1, out_channels=32, kernel_size=3, stride=1, padding=1)

    def forward(self, x):
        return self.conv1(x)

# Create an instance of the model and input data
model = SimpleModel()
input_data = torch.randn(1, 1, 10)  # Batch size of 1, 1 channel, sequence length of 10

# Perform a forward pass
output = model(input_data)
print(output.shape)  # Should print: torch.Size([1, 32, 10])