import torch
from torch import nn

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
input_seq = torch.randn(5, 3, input_size)  # (sequence length, batch size, input size)
output, _ = model(input_seq)

print(output.shape)  # Should be (5, 3, 20)