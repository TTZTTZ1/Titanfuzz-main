import torch
import torch.nn as nn

# Define the GRU model
class SimpleGRU(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers):
        super(SimpleGRU, self).__init__()
        self.gru = nn.GRU(input_size, hidden_size, num_layers, batch_first=True)

    def forward(self, x, h0=None):
        output, _ = self.gru(x, h0)
        return output

# Example usage
input_size = 10
hidden_size = 20
num_layers = 2
batch_size = 3
sequence_length = 5

# Create random input data
x = torch.randn(sequence_length, batch_size, input_size)

# Initialize hidden state
h0 = torch.randn(num_layers, batch_size, hidden_size)

# Create the GRU model
gru_model = SimpleGRU(input_size, hidden_size, num_layers)

# Forward pass
output = gru_model(x, h0)
print(output.shape)  # Should be (5, 3, 20)