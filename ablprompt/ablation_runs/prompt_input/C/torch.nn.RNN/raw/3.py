import torch
import torch.nn as nn

# Define the RNN model
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, nonlinearity='tanh', dropout=0.0, bidirectional=False):
        super(SimpleRNN, self).__init__()
        self.rnn = nn.RNN(input_size=input_size, hidden_size=hidden_size, num_layers=num_layers, nonlinearity=nonlinearity, dropout=dropout, bidirectional=bidirectional)
    
    def forward(self, x):
        # Initialize hidden state
        h0 = torch.zeros(self.rnn.num_layers, x.size(0), self.rnn.hidden_size).to(x.device)
        
        # Forward propagate RNN
        out, _ = self.rnn(x, h0)
        return out

# Example usage
input_size = 10
hidden_size = 20
num_layers = 2
sequence_length = 5
batch_size = 3

# Create random input data
x = torch.randn(sequence_length, batch_size, input_size)

# Create the RNN model instance
model = SimpleRNN(input_size, hidden_size, num_layers)

# Forward pass
output = model(x)
print(output.shape)  # Should print: torch.Size([5, 3, 40])