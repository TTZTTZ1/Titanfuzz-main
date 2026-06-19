import torch
from torch import nn

# Define a simple model using ConvTranspose1d
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.conv_transpose = nn.ConvTranspose1d(in_channels=3, out_channels=64, kernel_size=5, stride=2, padding=1)

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model and input tensor
model = SimpleModel()
input_tensor = torch.randn(1, 3, 10)  # Batch size 1, 3 channels, sequence length 10

# Forward pass through the model
output_tensor = model(input_tensor)
print(output_tensor.shape)  # Should print the shape of the output tensor