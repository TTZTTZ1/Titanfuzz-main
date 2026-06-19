import torch
import torch.nn as nn
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence

# Define the GRU model
class GRUNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, bidirectional=False):
        super(GRUNet, self).__init__()
        self.gru = nn.GRU(input_size, hidden_size, num_layers, bidirectional=bidirectional)
    
    def forward(self, x, lengths):
        # Pack the input sequence
        x = pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=False)
        # Forward through GRU
        out, _ = self.gru(x)
        # Unpack the output sequence
        out, _ = pad_packed_sequence(out, batch_first=True)
        return out

# Example usage
input_size = 10
hidden_size = 20
num_layers = 2
batch_size = 3
seq_len = 5
bidirectional = True

# Create dummy data
x = torch.randn(seq_len, batch_size, input_size)
lengths = [seq_len] * batch_size  # All sequences have the same length for simplicity

# Initialize the model
model = GRUNet(input_size, hidden_size, num_layers, bidirectional)

# Forward pass
output = model(x, lengths)
print(output.shape)  # Should be (seq_len, batch_size, hidden_size * (2 if bidirectional else 1))