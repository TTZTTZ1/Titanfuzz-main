import torch
import torch.nn as nn

# Define a simple model with a Linear layer
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.linear_layer = nn.Linear(in_features=784, out_features=10, bias=False)

    def forward(self, x):
        return self.linear_layer(x)

# Create an instance of the model
model = SimpleModel()

# Generate some random input data
input_data = torch.randn(64, 784)

# Forward pass through the model
output = model(input_data)

print(output.shape)  # Expected output shape: [64, 10]