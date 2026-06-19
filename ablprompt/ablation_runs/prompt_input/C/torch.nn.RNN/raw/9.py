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
batch_size = 3
sequence_length = 5

# Create an instance of the RNN model
rnn_model = SimpleRNN(input_size, hidden_size, num_layers)

# Generate random input data
x = torch.randn(sequence_length, batch_size, input_size)

# Forward pass through the RNN
output = rnn_model(x)

print(output.shape)  # Expected output shape: (sequence_length, batch_size, hidden_size)