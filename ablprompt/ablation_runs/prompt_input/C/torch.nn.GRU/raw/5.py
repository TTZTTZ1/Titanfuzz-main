import torch
import torch.nn as nn

# Define the GRU model
gru = nn.GRU(input_size=10, hidden_size=20, num_layers=2, batch_first=True, bidirectional=True)

# Create some random input data
input_data = torch.randn(5, 3, 10)  # (seq_len, batch, input_size)

# Initialize hidden state
h0 = torch.randn(4, 3, 20)  # (num_layers * num_directions, batch, hidden_size)

# Forward pass through the GRU
output, hn = gru(input_data, h0)

print(output.shape)  # Should be (5, 3, 40) since it's bidirectional
print(hn.shape)      # Should be (4, 3, 20)