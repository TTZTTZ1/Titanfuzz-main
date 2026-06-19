import torch
import torch.nn as nn

# Define the RNN model
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, bidirectional):
        super(SimpleRNN, self).__init__()
        self.rnn = nn.RNN(input_size, hidden_size, num_layers, nonlinearity='tanh', bidirectional=bidirectional)
    
    def forward(self, x):
        h0 = torch.zeros(self.rnn.num_layers * (2 if self.rnn.bidirectional else 1), x.size(0), self.rnn.hidden_size).to(x.device)
        out, _ = self.rnn(x, h0)
        return out

# Create an instance of the RNN model
input_size = 10
hidden_size = 20
num_layers = 2
bidirectional = True
model = SimpleRNN(input_size, hidden_size, num_layers, bidirectional)

# Prepare some input data
batch_size = 5
seq_length = 3
input_data = torch.randn(seq_length, batch_size, input_size)

# Forward pass through the RNN
output = model(input_data)
print(output.shape)  # Should be (seq_length, batch_size, hidden_size * (2 if bidirectional else 1))