import torch
import torch.nn as nn

# Define an RNN model
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers):
        super(SimpleRNN, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.rnn = nn.RNN(input_size, hidden_size, num_layers, batch_first=True)
    
    def forward(self, x):
        # Initialize hidden state with zeros
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        
        # Forward propagate RNN
        out, _ = self.rnn(x, h0)
        return out

# Example usage
input_size = 10
hidden_size = 20
num_layers = 2
batch_size = 3
seq_length = 5

# Create a random input tensor
x = torch.randn(batch_size, seq_length, input_size)

# Create an instance of the RNN model
rnn_model = SimpleRNN(input_size, hidden_size, num_layers)

# Forward pass through the RNN
output = rnn_model(x)
print(output.shape)  # Should print: torch.Size([3, 5, 20])