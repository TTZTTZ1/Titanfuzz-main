import torch
from torch.nn import GRU

# Define the GRU model
gru = GRU(input_size=10, hidden_size=20, num_layers=2, batch_first=True, bidirectional=True)

# Create random input tensor
input_tensor = torch.randn(5, 3, 10)  # (seq_len, batch, input_size)

# Forward pass through the GRU
output, hn = gru(input_tensor)

print("Output:", output.shape)
print("Final Hidden State:", hn.shape)