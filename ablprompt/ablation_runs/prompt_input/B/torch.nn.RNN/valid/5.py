import torch
import torch.nn as nn

# Define the RNN model
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, bidirectional):
        super(SimpleRNN, self).__init__()
        self.rnn = nn.RNN(input_size, hidden_size, num_layers, nonlinearity='tanh', batch_first=True, bidirectional=bidirectional)
    
    def forward(self, x, hx=None):
        out, _ = self.rnn(x, hx)
        return out

# Create an instance of the RNN model
input_size = 10
hidden_size = 20
num_layers = 2
bidirectional = True
model = SimpleRNN(input_size, hidden_size, num_layers, bidirectional)

# Prepare some dummy input data
batch_size = 5
sequence_length = 3
x = torch.randn(sequence_length, batch_size, input_size)

# Forward pass through the RNN
output = model(x)
print(output.shape)  # Should be (3, 5, 40) for bidirectional RNN