import torch
import torch.nn as nn

# Define a simple model using ConvTranspose2d for upsampling
class UpsampleModel(nn.Module):
    def __init__(self):
        super(UpsampleModel, self).__init__()
        self.conv_transpose = nn.ConvTranspose2d(in_channels=3, out_channels=64, kernel_size=4, stride=2, padding=1)

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model and run a dummy input through it
model = UpsampleModel()
dummy_input = torch.randn(1, 3, 32, 32)
output = model(dummy_input)
print(output.shape)  # Expected output shape: torch.Size([1, 64, 64, 64])