import torch
import torch.nn as nn

# Define the RNN model
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, nonlinearity='tanh'):
        super(SimpleRNN, self).__init__()
        self.rnn = nn.RNN(input_size, hidden_size, num_layers, nonlinearity=nonlinearity)
    
    def forward(self, x, hx=None):
        return self.rnn(x, hx)

# Example usage
input_size = 10
hidden_size = 20
num_layers = 2
nonlinearity = 'tanh'

model = SimpleRNN(input_size, hidden_size, num_layers, nonlinearity)
input_data = torch.randn(5, 3, input_size)  # (sequence length, batch size, input size)
output, hidden_state = model(input_data)

print("Output:", output.shape)
print("Hidden State:", hidden_state.shape)