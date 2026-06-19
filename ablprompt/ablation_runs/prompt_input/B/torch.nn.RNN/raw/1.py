import torch
from torch import nn

# Define the RNN model
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers=1, nonlinearity='tanh'):
        super(SimpleRNN, self).__init__()
        self.rnn = nn.RNN(input_size, hidden_size, num_layers, nonlinearity=nonlinearity)
    
    def forward(self, x, hx=None):
        return self.rnn(x, hx)

# Initialize the model
input_size = 10
hidden_size = 20
model = SimpleRNN(input_size, hidden_size)

# Create dummy input data
batch_size = 5
sequence_length = 3
input_data = torch.randn(sequence_length, batch_size, input_size)

# Forward pass
output, _ = model(input_data)
print(output.shape)  # Should be (sequence_length, batch_size, hidden_size)