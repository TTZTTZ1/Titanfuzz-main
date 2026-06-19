import torch
import torch.nn as nn

# Define a simple GRU model
class SimpleGRU(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers):
        super(SimpleGRU, self).__init__()
        self.gru = nn.GRU(input_size, hidden_size, num_layers)
    
    def forward(self, x):
        out, _ = self.gru(x)
        return out

# Example usage of the SimpleGRU model
input_size = 10
hidden_size = 20
num_layers = 2
batch_size = 3
seq_length = 5

model = SimpleGRU(input_size, hidden_size, num_layers)

# Create a random input tensor
x = torch.randn(seq_length, batch_size, input_size)

# Forward pass through the model
output = model(x)

print(output.shape)  # Should be (seq_length, batch_size, hidden_size)