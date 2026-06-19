import torch
import torch.nn as nn

# Define a simple model with LayerNorm
class SimpleModel(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(SimpleModel, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.ln = nn.LayerNorm(hidden_size)
        self.fc2 = nn.Linear(hidden_size, input_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.ln(x)
        x = self.fc2(x)
        return x

# Create a model instance and input tensor
model = SimpleModel(10, 20)
input_tensor = torch.randn(3, 10)  # Batch size 3, input size 10

# Forward pass through the model
output = model(input_tensor)
print(output.shape)  # Should be [3, 10]