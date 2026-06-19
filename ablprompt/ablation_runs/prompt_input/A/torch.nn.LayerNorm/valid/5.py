import torch
import torch.nn as nn

# Define a simple model using LayerNorm
class SimpleModel(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(SimpleModel, self).__init__()
        self.linear = nn.Linear(input_size, hidden_size)
        self.layer_norm = nn.LayerNorm(hidden_size)

    def forward(self, x):
        x = self.linear(x)
        x = self.layer_norm(x)
        return x

# Create an instance of the model and some dummy input
model = SimpleModel(input_size=10, hidden_size=20)
input_data = torch.randn(5, 10)  # Batch size of 5, input size of 10

# Forward pass through the model
output = model(input_data)
print(output)