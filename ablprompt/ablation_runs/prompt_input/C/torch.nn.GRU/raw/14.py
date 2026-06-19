import torch
import torch.nn as nn

# Define the GRU model
gru = nn.GRU(input_size=128, hidden_size=64, num_layers=2, batch_first=True, bidirectional=True)

# Create a random input tensor
input_tensor = torch.randn(10, 32, 128)  # (seq_len, batch, input_size)

# Initialize hidden state
h0 = torch.zeros(4, 32, 64)  # (num_layers * num_directions, batch, hidden_size)

# Forward pass through the GRU
output, hn = gru(input_tensor, h0)

print(output.shape)  # Should be (seq_len, batch, num_directions * hidden_size)
print(hn.shape)      # Should be (num_layers * num_directions, batch, hidden_size)