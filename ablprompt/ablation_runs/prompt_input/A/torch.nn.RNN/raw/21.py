import torch
import torch.nn as nn

# Define an RNN model
class SimpleRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers):
        super(SimpleRNN, self).__init__()
        self.rnn = nn.RNN(input_size, hidden_size, num_layers, batch_first=True)
    
    def forward(self, x):
        out, _ = self.rnn(x)
        return out

# Example usage
input_size = 10
hidden_size = 20
num_layers = 2
batch_size = 3
seq_length = 5

model = SimpleRNN(input_size, hidden_size, num_layers)
input_data = torch.randn(batch_size, seq_length, input_size)

output = model(input_data)
print(output.shape)  # Should print: torch.Size([3, 5, 20])