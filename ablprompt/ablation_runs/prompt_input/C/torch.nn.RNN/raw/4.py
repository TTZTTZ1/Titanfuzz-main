import torch
import torch.nn as nn

# Define the RNN model
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, nonlinearity='tanh'):
        super(SimpleRNN, self).__init__()
        self.rnn = nn.RNN(input_size, hidden_size, num_layers, nonlinearity=nonlinearity)
    
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
nonlinearity = 'relu'

model = SimpleRNN(input_size, hidden_size, num_layers, nonlinearity)
input_seq = torch.randn(5, 3, input_size)  # Sequence length, Batch size, Input size
output = model(input_seq)

print(output.shape)  # Should be (5, 3, 20)