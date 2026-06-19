import torch
import torch.nn as nn

# Define the RNN model
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, nonlinearity='tanh'):
        super(SimpleRNN, self).__init__()
        self.rnn = nn.RNN(input_size, hidden_size, num_layers, nonlinearity=nonlinearity)

    def forward(self, x, hx=None):
        out, _ = self.rnn(x, hx)
        return out

# Example usage
input_size = 10
hidden_size = 20
num_layers = 2
rnn_model = SimpleRNN(input_size, hidden_size, num_layers)

# Create dummy input
batch_size = 3
seq_length = 5
dummy_input = torch.randn(seq_length, batch_size, input_size)

# Forward pass
output = rnn_model(dummy_input)
print(output.shape)  # Should be (seq_length, batch_size, hidden_size)