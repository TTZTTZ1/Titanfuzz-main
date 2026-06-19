import torch
import torch.nn as nn

# Define a simple model with LayerNorm
class SimpleModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleModel, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.ln1 = nn.LayerNorm(hidden_size)
        self.fc2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = self.fc1(x)
        x = self.ln1(x)
        x = self.fc2(x)
        return x

# Example usage
model = SimpleModel(input_size=784, hidden_size=128, output_size=10)
input_data = torch.randn(32, 784)  # Batch size 32, input size 784
output = model(input_data)
print(output.shape)  # Should be [32, 10]