import torch
import torch.nn as nn

# Define the RNN model
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers=1, nonlinearity='tanh'):
        super(SimpleRNN, self).__init__()
        self.rnn = nn.RNN(input_size, hidden_size, num_layers=num_layers, nonlinearity=nonlinearity)
    
    def forward(self, x, hx=None):
        out, h_n = self.rnn(x, hx)
        return out, h_n

# Create an instance of the RNN model
input_size = 10
hidden_size = 20
rnn_model = SimpleRNN(input_size, hidden_size)

# Prepare input data
batch_size = 3
sequence_length = 5
input_data = torch.randn(sequence_length, batch_size, input_size)

# Forward pass
output, hidden_state = rnn_model(input_data)

print("Output shape:", output.shape)
print("Hidden state shape:", hidden_state.shape)