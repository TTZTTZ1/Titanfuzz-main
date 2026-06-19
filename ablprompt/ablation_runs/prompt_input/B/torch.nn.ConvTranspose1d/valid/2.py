import torch
from torch import nn

# Define a simple model using ConvTranspose1d
class UpsampleModel(nn.Module):
    def __init__(self):
        super(UpsampleModel, self).__init__()
        self.conv_transpose = nn.ConvTranspose1d(in_channels=16, out_channels=8, kernel_size=3, stride=2, padding=1)

    def forward(self, x):
        return self.conv_transpose(x)

# Create an instance of the model and run it
model = UpsampleModel()
input_tensor = torch.randn(1, 16, 5)  # Batch size 1, 16 input channels, sequence length 5
output_tensor = model(input_tensor)
print(output_tensor.shape)  # Expected shape: torch.Size([1, 8, 9])