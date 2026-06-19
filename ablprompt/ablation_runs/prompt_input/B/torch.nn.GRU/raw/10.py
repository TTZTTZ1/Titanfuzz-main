import torch
from torch.nn import GRU, Linear
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence

# Define the GRU model
class GRUNet(torch.nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(GRUNet, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.gru = GRU(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = Linear(hidden_size, output_size)

    def forward(self, x, lengths):
        # Pack the input sequence
        x = pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=False)
        # Forward propagate through GRU
        out, _ = self.gru(x)
        # Unpack the output sequence
        out, _ = pad_packed_sequence(out, batch_first=True)
        # Apply fully connected layer
        out = self.fc(out[:, -1, :])
        return out

# Example usage
input_size = 10
hidden_size = 20
num_layers = 2
output_size = 1
batch_size = 3
seq_lengths = [5, 4, 3]

# Create an instance of the model
model = GRUNet(input_size, hidden_size, num_layers, output_size).to('cuda')

# Generate random input data
x = torch.randn(batch_size, max(seq_lengths), input_size).to('cuda')
lengths = torch.tensor(seq_lengths).to('cuda')

# Forward pass
output = model(x, lengths)
print(output)