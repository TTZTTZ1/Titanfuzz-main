import torch
from torch.nn import GRU, Linear
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence

# Define the GRU model
class SimpleGRU(torch.nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(SimpleGRU, self).__init__()
        self.gru = GRU(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = Linear(hidden_size, output_size)

    def forward(self, x, lengths):
        x = pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=False)
        out, _ = self.gru(x)
        out, _ = pad_packed_sequence(out, batch_first=True)
        out = self.fc(out[:, -1, :])  # Use only the last time step's output
        return out

# Example usage
input_size = 10
hidden_size = 20
num_layers = 2
output_size = 1
batch_size = 3
seq_lengths = [5, 4, 3]

model = SimpleGRU(input_size, hidden_size, num_layers, output_size)
input_data = torch.randn(batch_size, max(seq_lengths), input_size)
output = model(input_data, seq_lengths)
print(output)