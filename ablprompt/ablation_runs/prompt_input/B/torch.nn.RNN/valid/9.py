import torch
import torch.nn as nn

# Define the RNN model
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, bidirectional):
        super(SimpleRNN, self).__init__()
        self.rnn = nn.RNN(input_size, hidden_size, num_layers, batch_first=True, bidirectional=bidirectional)
    
    def forward(self, x):
        h0 = torch.zeros(num_layers * (2 if bidirectional else 1), x.size(0), hidden_size).to(x.device)
        out, _ = self.rnn(x, h0)
        return out

# Create an instance of the RNN model
input_size = 10
hidden_size = 20
num_layers = 2
bidirectional = True
model = SimpleRNN(input_size, hidden_size, num_layers, bidirectional)

# Generate random input data
batch_size = 5
sequence_length = 3
x = torch.randn(batch_size, sequence_length, input_size)

# Forward pass through the RNN
output = model(x)
print(output.shape)  # Should be (batch_size, sequence_length, hidden_size * (2 if bidirectional else 1))