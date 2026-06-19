import torch
from torch import nn

# Define a simple model using ConvTranspose2d
class SimpleDeconvNet(nn.Module):
    def __init__(self):
        super(SimpleDeconvNet, self).__init__()
        # Initialize the transposed convolution layer
        self.deconv = nn.ConvTranspose2d(in_channels=1, out_channels=3, kernel_size=3, stride=2, padding=1)

    def forward(self, x):
        return self.deconv(x)

# Create an instance of the model and input tensor
model = SimpleDeconvNet()
input_tensor = torch.randn(1, 1, 4, 4)  # Batch size 1, channels 1, height 4, width 4

# Perform the forward pass
output_tensor = model(input_tensor)
print(output_tensor.shape)  # Output shape should be [1, 3, 8, 8]