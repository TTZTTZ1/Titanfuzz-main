import torch
from torch import nn

# Define a simple GRU model
class SimpleGRU(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers=1):
        super(SimpleGRU, self).__init__()
        self.gru = nn.GRU(input_size, hidden_size, num_layers)

    def forward(self, x):
        out, _ = self.gru(x)
        return out

# Example usage
input_size = 10
hidden_size = 20
batch_size = 5
seq_length = 3

model = SimpleGRU(input_size, hidden_size)
inputs = torch.randn(seq_length, batch_size, input_size)  # Input shape: (seq_len, batch, input_size)
outputs = model(inputs)
print(outputs.shape)  # Output shape: (seq_len, batch, hidden_size)