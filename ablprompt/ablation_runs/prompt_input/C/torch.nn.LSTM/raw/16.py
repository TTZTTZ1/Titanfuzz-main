import torch
import torch.nn as nn

# Define the LSTM model
lstm = nn.LSTM(
    input_size=10,
    hidden_size=20,
    num_layers=2,
    bias=True,
    batch_first=False,
    dropout=0.5,
    bidirectional=True,
    proj_size=10
)

# Create dummy input tensor
input_tensor = torch.randn(5, 3, 10)

# Initialize hidden and cell states
h0 = torch.randn(4, 3, 10)  # 2 layers * 2 directions * hidden_size
c0 = torch.randn(4, 3, 10)

# Forward pass through the LSTM
output, (hn, cn) = lstm(input_tensor, (h0, c0))

print("Output:", output.shape)
print("Final Hidden State:", hn.shape)
print("Final Cell State:", cn.shape)