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
seq_len = 5

# Create random input data
x = torch.randn(seq_len, batch_size, input_size)

# Initialize the RNN model
model = SimpleRNN(input_size, hidden_size, num_layers)

# Forward pass
output = model(x)
print(output.shape)  # Should be (seq_len, batch_size, hidden_size)