import torch
import torch.nn as nn

# Define a simple model using ConvTranspose3d
class SimpleUpsampleModel(nn.Module):
    def __init__(self):
        super(SimpleUpsampleModel, self).__init__()
        self.conv_transpose = nn.ConvTranspose3d(in_channels=16, out_channels=33, kernel_size=3, stride=2, padding=1)

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model
model = SimpleUpsampleModel()

# Generate a random input tensor
input_tensor = torch.randn(20, 16, 10, 50, 100)

# Forward pass through the model
output_tensor = model(input_tensor)

print(output_tensor.shape)