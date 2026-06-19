import torch
import torch.nn as nn

# Define the RNN model
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, nonlinearity='tanh', bidirectional=False, dropout=0.0):
        super(SimpleRNN, self).__init__()
        self.rnn = nn.RNN(input_size=input_size, hidden_size=hidden_size, num_layers=num_layers, 
                          nonlinearity=nonlinearity, bidirectional=bidirectional, dropout=dropout)
    
    def forward(self, x, hx=None):
        out, hn = self.rnn(x, hx)
        return out, hn

# Example usage
input_size = 10
hidden_size = 20
num_layers = 2
batch_size = 5
sequence_length = 3

# Create an instance of the RNN model
model = SimpleRNN(input_size, hidden_size, num_layers)

# Generate random input data
x = torch.randn(sequence_length, batch_size, input_size)

# Forward pass through the RNN model
output, hidden_state = model(x)

print("Output:", output.shape)
print("Hidden State:", hidden_state.shape)