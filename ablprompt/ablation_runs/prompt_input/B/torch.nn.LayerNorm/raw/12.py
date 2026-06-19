import torch
from torch import nn

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

# Example usage
model = SimpleModel(input_size=10, hidden_size=20)
input_data = torch.randn(32, 10)  # Batch size 32, input size 10
output = model(input_data)
print(output.shape)  # Should be [32, 10]