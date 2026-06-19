import torch
import torch.nn as nn
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence

# Define the GRU model
class GRUNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, bidirectional=False):
        super(GRUNet, self).__init__()
        self.gru = nn.GRU(input_size, hidden_size, num_layers, batch_first=True, bidirectional=bidirectional)

    def forward(self, x, lengths):
        # Pack the input sequence
        packed_input = pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=False)
        # Forward pass through GRU
        packed_output, _ = self.gru(packed_input)
        # Unpack the output sequence
        output, _ = pad_packed_sequence(packed_output, batch_first=True)
        return output

# Example usage
if __name__ == "__main__":
    input_size = 10
    hidden_size = 20
    num_layers = 2
    bidirectional = True
    batch_size = 3
    seq_lengths = [5, 4, 6]

    gru_net = GRUNet(input_size, hidden_size, num_layers, bidirectional)
    input_data = torch.randn(batch_size, max(seq_lengths), input_size)
    output = gru_net(input_data, seq_lengths)
    print(output.shape)  # Should be (batch_size, max_seq_length, hidden_size * (2 if bidirectional else 1))