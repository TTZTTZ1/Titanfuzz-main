import torch
import torch.nn as nn

# Define the RNN model
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers=1, nonlinearity='tanh'):
        super(SimpleRNN, self).__init__()
        self.rnn = nn.RNN(input_size, hidden_size, num_layers=num_layers, nonlinearity=nonlinearity)
    
    def forward(self, x, hx=None):
        out, _ = self.rnn(x, hx)
        return out

# Example usage
input_size = 10
hidden_size = 20
num_layers = 2
nonlinearity = 'relu'
batch_size = 5
sequence_length = 3

# Create an instance of the RNN model
model = SimpleRNN(input_size, hidden_size, num_layers, nonlinearity)

# Generate random input data
x = torch.randn(sequence_length, batch_size, input_size)

# Forward pass through the RNN
output = model(x)

print(output.shape)  # Should be (sequence_length, batch_size, hidden_size)