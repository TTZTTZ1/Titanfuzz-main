import torch
import torch.nn as nn

# Define a simple model using Conv1d
class SimpleConvModel(nn.Module):
    def __init__(self):
        super(SimpleConvModel, self).__init__()
        self.conv1 = nn.Conv1d(in_channels=16, out_channels=33, kernel_size=3, stride=2, padding=1, bias=True)
    
    def forward(self, x):
        return self.conv1(x)

# Create an instance of the model and a random input tensor
model = SimpleConvModel()
input_tensor = torch.randn(20, 16, 50)

# Forward pass through the model
output_tensor = model(input_tensor)

print(output_tensor.shape)  # Expected output shape: torch.Size([20, 33, 25])