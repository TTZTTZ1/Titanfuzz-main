import torch
import torch.nn as nn

# Define a simple model using Conv1d
class SimpleConvNet(nn.Module):
    def __init__(self):
        super(SimpleConvNet, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=16, out_channels=33, kernel_size=3, stride=2, padding=1, dilation=1, groups=1, bias=True, padding_mode='zeros')
    
    def forward(self, x):
        return self.conv1(x)

# Create a random input tensor
input_tensor = torch.randn(20, 16, 50)

# Instantiate the model and perform forward pass
model = SimpleConvNet()
output_tensor = model(input_tensor)

print(output_tensor.shape)