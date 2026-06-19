import torch
import torch.nn as nn

# Define an RNN model
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
input_data = torch.randn(5, 3, input_size)  # Sequence length, batch size, input size
output, _ = model(input_data)

print(output.shape)  # Should be (5, 3, hidden_size)