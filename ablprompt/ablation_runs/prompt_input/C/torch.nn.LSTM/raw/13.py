import torch
import torch.nn as nn

# Define the LSTM model
lstm = nn.LSTM(
    input_size=10,
    hidden_size=20,
    num_layers=2,
    batch_first=True,
    dropout=0.5,
    bidirectional=False,
    proj_size=10
)

# Create a random input tensor
input_tensor = torch.randn(5, 3, 10)  # (seq_len=5, batch=3, input_size=10)

# Initialize hidden and cell states
h0 = torch.randn(2 * lstm.num_layers, input_tensor.size(0), lstm.hidden_size)  # (num_layers*num_directions, batch, hidden_size)
c0 = torch.randn(2 * lstm.num_layers, input_tensor.size(0), lstm.hidden_size)  # (num_layers*num_directions, batch, hidden_size)

# Forward pass through the LSTM
output, (hn, cn) = lstm(input_tensor, (h0, c0))

print("Output:", output.shape)
print("Hidden State:", hn.shape)
print("Cell State:", cn.shape)