import torch
import torch.nn as nn

# Define the GRU model
gru = nn.GRU(
    input_size=10,
    hidden_size=20,
    num_layers=2,
    batch_first=True,
    bidirectional=True,
    dropout=0.5
)

# Create random input data
batch_size = 3
sequence_length = 5
input_data = torch.randn(sequence_length, batch_size, 10)

# Initialize hidden state
h0 = torch.randn(4, batch_size, 20)  # 2 layers * 2 directions * hidden_size

# Forward pass through the GRU
output, hn = gru(input_data, h0)

print("Output:", output.shape)
print("Hidden State:", hn.shape)