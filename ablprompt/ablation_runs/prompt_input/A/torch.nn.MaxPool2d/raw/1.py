import torch
import torch.nn as nn

# Define a simple model using MaxPool2d
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.pool = nn.MaxPool2d(kernel_size=2, stride=1, padding=0)

    def forward(self, x):
        return self.pool(x)

# Create an instance of the model and input tensor
model = SimpleModel()
input_tensor = torch.randn(1, 1, 4, 4)  # Batch size 1, 1 channel, 4x4 image

# Forward pass through the model
output_tensor = model(input_tensor)
print(output_tensor)