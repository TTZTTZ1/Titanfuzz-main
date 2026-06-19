import torch
import torch.nn as nn

# Define a simple RNN model
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, nonlinearity='tanh'):
        super(SimpleRNN, self).__init__()
        self.rnn = nn.RNN(input_size, hidden_size, num_layers, nonlinearity=nonlinearity)
    
    def forward(self, x, hx=None):
        out, _ = self.rnn(x, hx)
        return out

# Create an instance of the RNN model
input_size = 10
hidden_size = 20
num_layers = 3
rnn_model = SimpleRNN(input_size, hidden_size, num_layers)

# Prepare some dummy input data
batch_size = 5
sequence_length = 8
input_data = torch.randn(sequence_length, batch_size, input_size)

# Forward pass through the RNN model
output = rnn_model(input_data)
print(output.shape)  # Should be (sequence_length, batch_size, hidden_size)