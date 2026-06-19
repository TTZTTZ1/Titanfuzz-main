import torch
import torch.nn as nn

# Define the GRU model
gru = nn.GRU(input_size=10, hidden_size=20, num_layers=2, batch_first=True, bidirectional=True)

# Create a random input tensor
input_tensor = torch.randn(5, 3, 10)  # (seq_len, batch, input_size)

# Initialize the hidden state
h0 = torch.randn(4, 3, 20)  # (num_layers * num_directions, batch, hidden_size)

# Forward pass through the GRU
output, hn = gru(input_tensor, h0)

print("Output:", output.shape)  # Should be (5, 3, 40)
print("Final Hidden State:", hn.shape)  # Should be (4, 3, 20)