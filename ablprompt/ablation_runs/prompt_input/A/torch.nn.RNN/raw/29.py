import torch
import torch.nn as nn

# Define an RNN model
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers):
        super(SimpleRNN, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.rnn = nn.RNN(input_size, hidden_size, num_layers, batch_first=True)

    def forward(self, x, h0):
        # Forward propagate RNN
        out, _ = self.rnn(x, h0)
        return out

# Example usage
input_size = 10
hidden_size = 20
num_layers = 2
batch_size = 3
seq_length = 5

# Create random input and initial hidden state
x = torch.randn(batch_size, seq_length, input_size)
h0 = torch.randn(num_layers, batch_size, hidden_size)

# Initialize the RNN model
model = SimpleRNN(input_size, hidden_size, num_layers)

# Forward pass through RNN
output = model(x, h0)
print(output.shape)  # Should print: torch.Size([3, 5, 20])