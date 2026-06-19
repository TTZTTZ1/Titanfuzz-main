import torch
import torch.nn as nn

# Define an RNN model
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers):
        super(SimpleRNN, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.rnn = nn.RNN(input_size, hidden_size, num_layers, batch_first=True)
    
    def forward(self, x, h0):
        out, _ = self.rnn(x, h0)
        return out

# Parameters
input_size = 10
hidden_size = 20
num_layers = 2
batch_size = 5
seq_length = 3

# Create an instance of the model
model = SimpleRNN(input_size, hidden_size, num_layers)

# Generate random input and initial hidden state
x = torch.randn(batch_size, seq_length, input_size)
h0 = torch.randn(num_layers, batch_size, hidden_size)

# Forward pass
output = model(x, h0)
print(output.shape)  # Should print: torch.Size([5, 3, 20])