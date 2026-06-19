import torch
import torch.nn as nn

# Define a simple model using ConvTranspose1d
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv_transpose = nn.ConvTranspose1d(in_channels=3, out_channels=64, kernel_size=5, stride=2)

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model and some input data
model = SimpleModel()
input_data = torch.randn(1, 3, 10)  # Batch size of 1, 3 channels, sequence length of 10

# Forward pass through the model
output = model(input_data)
print(output.shape)  # Should print: torch.Size([1, 64, 23])