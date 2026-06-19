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
model = SimpleModel(10, 20, 3)
input_data = torch.randn(5, 10)  # Batch size of 5, input size of 10
output = model(input_data)
print(output.shape)  # Should be [5, 3]