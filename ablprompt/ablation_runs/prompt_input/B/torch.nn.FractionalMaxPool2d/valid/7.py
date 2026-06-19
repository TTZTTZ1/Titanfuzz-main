import torch
import torch.nn as nn

# Define a simple model using FractionalMaxPool2d
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.pool = nn.FractionalMaxPool2d(kernel_size=3, output_size=(4, 4), return_indices=True)

    def forward(self, x):
        out, indices = self.pool(x)
        return out, indices

# Create an instance of the model and a random input tensor
model = SimpleModel()
input_tensor = torch.randn(1, 1, 8, 8)

# Forward pass through the model
output, indices = model(input_tensor)

print("Output:", output)
print("Indices:", indices)