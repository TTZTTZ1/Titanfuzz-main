import torch
import torch.nn as nn

# Define the LSTM model
lstm = nn.LSTM(
    input_size=10,
    hidden_size=20,
    num_layers=2,
    batch_first=True,
    bidirectional=False,
    dropout=0.5,
    proj_size=10
)

# Create random input tensor
input_tensor = torch.randn(5, 3, 10)  # (seq_len=5, batch=3, input_size=10)

# Initialize hidden and cell states
h0 = torch.randn(4, 3, 20)  # (num_layers*directions, batch, hidden_size)
c0 = torch.randn(4, 3, 20)

# Forward pass through the LSTM
output, (hn, cn) = lstm(input_tensor, (h0, c0))

print("Output:", output.shape)
print("Hidden State:", hn.shape)
print("Cell State:", cn.shape)