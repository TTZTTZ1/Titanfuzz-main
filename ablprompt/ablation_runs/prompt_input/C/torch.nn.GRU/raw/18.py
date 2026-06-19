import torch
import torch.nn as nn

# Define the GRU model
gru = nn.GRU(input_size=128, hidden_size=64, num_layers=2, batch_first=True, bidirectional=True)

# Create some random input data
input_data = torch.randn(10, 32, 128)  # (sequence length, batch size, input size)

# Initialize hidden state
h0 = torch.zeros(4, 32, 64)  # (num_layers * num_directions, batch_size, hidden_size)

# Forward pass through the GRU
output, hn = gru(input_data, h0)

print("Output shape:", output.shape)
print("Hidden state shape:", hn.shape)