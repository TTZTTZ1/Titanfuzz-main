import torch
import torch.nn as nn

# Define an RNN model
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers=1, nonlinearity='tanh'):
        super(SimpleRNN, self).__init__()
        self.rnn = nn.RNN(input_size, hidden_size, num_layers=num_layers, nonlinearity=nonlinearity)
    
    def forward(self, x):
        h0 = torch.zeros(num_layers, x.size(0), hidden_size).to(x.device)
        out, _ = self.rnn(x, h0)
        return out

# Example usage
input_size = 10
hidden_size = 20
num_layers = 2
nonlinearity = 'relu'

model = SimpleRNN(input_size, hidden_size, num_layers, nonlinearity)

# Create random input data
batch_size = 5
sequence_length = 3
x = torch.randn(sequence_length, batch_size, input_size)

# Forward pass
output = model(x)
print(output.shape)  # Should be (sequence_length, batch_size, hidden_size)