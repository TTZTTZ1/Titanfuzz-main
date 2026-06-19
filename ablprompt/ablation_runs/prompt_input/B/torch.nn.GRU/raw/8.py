import torch
import torch.nn as nn

# Define the GRU model
gru = nn.GRU(
    input_size=10,
    hidden_size=20,
    num_layers=2,
    bias=True,
    batch_first=True,
    dropout=0.5,
    bidirectional=False,
    device='cpu',
    dtype=torch.float32
)

# Create a random input tensor
input_tensor = torch.randn(5, 3, 10)  # (seq_len, batch, input_size)

# Initialize hidden state
h0 = torch.randn(2, 3, 20)  # (num_layers, batch, hidden_size)

# Forward pass through the GRU
output, hn = gru(input_tensor, h0)

print("Output:", output.shape)
print("Hidden State:", hn.shape)