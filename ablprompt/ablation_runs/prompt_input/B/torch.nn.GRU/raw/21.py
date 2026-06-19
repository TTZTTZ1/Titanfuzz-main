import torch
import torch.nn as nn
import torch.nn.utils.rnn as rnn_utils

# Define the GRU model
gru = nn.GRU(input_size=10, hidden_size=20, num_layers=2, batch_first=True, bidirectional=True)

# Create random input data
input_data = torch.randn(5, 3, 10)  # (seq_len, batch, input_size)

# Pack the input data if it contains variable-length sequences
lengths = torch.tensor([5, 4, 3])
packed_input = rnn_utils.pack_padded_sequence(input_data, lengths, batch_first=True)

# Initialize hidden state
h0 = torch.randn(4, 3, 20)  # (num_layers * num_directions, batch, hidden_size)

# Forward pass through the GRU
output, hn = gru(packed_input, h0)

# Unpack the output if needed
output, _ = rnn_utils.pad_packed_sequence(output, batch_first=True)

print("Output:", output)
print("Final Hidden State:", hn)