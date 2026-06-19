import torch
import torch.nn as nn

# Define a simple neural network model with LayerNorm
class SimpleModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleModel, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.ln1 = nn.LayerNorm(hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.ln1(x)
        x = self.fc2(x)
        return x

# Create an instance of the model
model = SimpleModel(input_size=10, hidden_size=20, output_size=1)

# Generate random input data
input_data = torch.randn(32, 10)

# Forward pass through the model
output = model(input_data)
print(output.shape)  # Should be [32, 1]