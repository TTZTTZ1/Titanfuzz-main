import torch
import torch.nn as nn
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence

# Define the GRU model
class GRUNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, bidirectional=False):
        super(GRUNet, self).__init__()
        self.gru = nn.GRU(input_size, hidden_size, num_layers, batch_first=True, bidirectional=bidirectional)

    def forward(self, x, lengths):
        # Pack the sequence
        packed_input = pack_padded_sequence(x, lengths, batch_first=True, enforce_sorted=False)
        # Forward pass through GRU
        packed_output, _ = self.gru(packed_input)
        # Unpack the sequence
        output, _ = pad_packed_sequence(packed_output, batch_first=True)
        return output

# Example usage
if __name__ == "__main__":
    input_size = 10
    hidden_size = 20
    num_layers = 2
    bidirectional = True

    gru_net = GRUNet(input_size, hidden_size, num_layers, bidirectional)
    input_tensor = torch.randn(5, 3, 10)  # (seq_len, batch, input_size)
    lengths = [5, 4, 3]  # Lengths of sequences in the batch

    output = gru_net(input_tensor, lengths)
    print(output.shape)  # Should be (5, 3, 40) for bidirectional GRU