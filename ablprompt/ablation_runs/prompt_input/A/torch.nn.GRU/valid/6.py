import torch
import torch.nn as nn

# Define a simple GRU model
class SimpleGRU(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers):
        super(SimpleGRU, self).__init__()
        self.gru = nn.GRU(input_size, hidden_size, num_layers)

    def forward(self, x):
        out, _ = self.gru(x)
        return out

# Example usage
input_size = 10
hidden_size = 20
num_layers = 2
batch_size = 5
seq_length = 3

model = SimpleGRU(input_size, hidden_size, num_layers)
input_data = torch.randn(seq_length, batch_size, input_size)
output = model(input_data)
print(output.shape)  # Should print: torch.Size([3, 5, 20])