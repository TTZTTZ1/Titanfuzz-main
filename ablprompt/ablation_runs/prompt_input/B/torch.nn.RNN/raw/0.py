import torch
import torch.nn as nn

# Define a simple RNN model
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, bidirectional):
        super(SimpleRNN, self).__init__()
        self.rnn = nn.RNN(input_size, hidden_size, num_layers, nonlinearity='relu', bidirectional=bidirectional)
    
    def forward(self, x):
        # Initialize hidden state
        h0 = torch.zeros(num_layers * (2 if bidirectional else 1), x.size(0), hidden_size).to(x.device)
        out, _ = self.rnn(x, h0)
        return out

# Example usage
input_size = 10
hidden_size = 20
num_layers = 2
bidirectional = True
batch_size = 5
sequence_length = 3

# Create an instance of the RNN model
model = SimpleRNN(input_size, hidden_size, num_layers, bidirectional)

# Generate random input data
input_data = torch.randn(sequence_length, batch_size, input_size)

# Forward pass through the RNN
output = model(input_data)
print(output.shape)  # Should be (sequence_length, batch_size, hidden_size * (2 if bidirectional else 1))