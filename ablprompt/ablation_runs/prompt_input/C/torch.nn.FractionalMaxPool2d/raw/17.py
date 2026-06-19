import torch
import torch.nn as nn

# Define a simple model with FractionalMaxPool2d
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.pool = nn.FractionalMaxPool2d(kernel_size=2, output_size=(7, 6), return_indices=True)

    def forward(self, x):
        x, indices = self.pool(x)
        return x, indices

# Create an instance of the model and an input tensor
model = SimpleModel()
input_tensor = torch.randn(1, 3, 14, 12)

# Forward pass through the model
output, indices = model(input_tensor)

print("Output:", output.shape)
print("Indices:", indices.shape)