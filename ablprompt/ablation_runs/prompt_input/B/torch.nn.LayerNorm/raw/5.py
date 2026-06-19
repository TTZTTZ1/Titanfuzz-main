import torch
import torch.nn as nn

# Define a simple model with LayerNorm
class SimpleModel(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(SimpleModel, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.ln1 = nn.LayerNorm(hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, input_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.ln1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# Create a sample input
input_tensor = torch.randn(32, 10)  # Batch size 32, input features 10

# Initialize the model
model = SimpleModel(10, 20)

# Forward pass
output = model(input_tensor)
print(output.shape)  # Should be [32, 10]