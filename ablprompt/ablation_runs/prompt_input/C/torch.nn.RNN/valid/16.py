import torch
import torch.nn as nn

# Define the RNN model
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers=1, nonlinearity='tanh'):
        super(SimpleRNN, self).__init__()
        self.rnn = nn.RNN(input_size, hidden_size, num_layers=num_layers, nonlinearity=nonlinearity)
    
    def forward(self, x, hx=None):
        return self.rnn(x, hx)

# Example usage
input_size = 10
hidden_size = 20
num_layers = 2
nonlinearity = 'relu'

model = SimpleRNN(input_size, hidden_size, num_layers, nonlinearity)

# Dummy input
batch_size = 5
seq_length = 3
x = torch.randn(seq_length, batch_size, input_size)

# Forward pass
output, h_n = model(x)

print("Output:", output.shape)
print("Final Hidden State:", h_n.shape)