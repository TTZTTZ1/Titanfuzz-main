import torch
from torch.nn import GRU
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence

# Define the model
gru = GRU(input_size=10, hidden_size=20, num_layers=2, batch_first=True, bidirectional=True)

# Create some random input data
batch_size = 3
sequence_length = 5
input_data = torch.randn(sequence_length, batch_size, 10)

# Pack the input data since it has variable lengths
lengths = [sequence_length] * batch_size
packed_input = pack_padded_sequence(input_data, lengths, batch_first=True, enforce_sorted=False)

# Initialize hidden state
h0 = torch.randn(4, batch_size, 20)  # 2 layers, bidirectional, so 4 hidden units

# Forward pass
output, h_n = gru(packed_input, h0)

# Unpack the output if needed
output, _ = pad_packed_sequence(output, batch_first=True)

print("Output shape:", output.shape)
print("Final hidden state shape:", h_n.shape)