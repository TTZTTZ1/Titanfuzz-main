import torch
import torch.nn as nn

# Define a simple model using ConvTranspose2d
class UpsampleModel(nn.Module):
    def __init__(self):
        super(UpsampleModel, self).__init__()
        self.conv_transpose = nn.ConvTranspose2d(in_channels=3, out_channels=64, kernel_size=4, stride=2, padding=1)

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model and run it on a random input
model = UpsampleModel()
input_tensor = torch.randn(1, 3, 32, 32)
output_tensor = model(input_tensor)

print(output_tensor.shape)