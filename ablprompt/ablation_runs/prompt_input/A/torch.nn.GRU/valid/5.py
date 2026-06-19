import torch
import torch.nn as nn

# Define the GRU model
class SimpleGRU(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers):
        super(SimpleGRU, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.gru = nn.GRU(input_size, hidden_size, num_layers, batch_first=True)
    
    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        out, _ = self.gru(x, h0)
        return out

# Example usage
input_size = 10
hidden_size = 20
num_layers = 2
batch_size = 5
sequence_length = 3

model = SimpleGRU(input_size, hidden_size, num_layers)
inputs = torch.randn(batch_size, sequence_length, input_size)

output = model(inputs)
print(output.shape)  # Should be [5, 3, 20]