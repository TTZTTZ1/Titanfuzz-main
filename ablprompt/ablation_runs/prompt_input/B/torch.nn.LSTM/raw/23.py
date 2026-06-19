import torch
import torch.nn as nn

# Define an LSTM model with multiple layers, dropout, and bidirectional processing
lstm = nn.LSTM(input_size=10, hidden_size=20, num_layers=3, batch_first=True, dropout=0.5, bidirectional=True)

# Create a random input tensor
input_tensor = torch.randn(5, 3, 10)  # (seq_len=5, batch=3, input_size=10)

# Initialize hidden and cell states
h0 = torch.randn(6, 3, 20)  # (num_layers*directions, batch, hidden_size)
c0 = torch.randn(6, 3, 20)

# Forward pass through the LSTM
output, (hn, cn) = lstm(input_tensor, (h0, c0))

print(output.shape)  # Should print torch.Size([5, 3, 40])
print(hn.shape)      # Should print torch.Size([6, 3, 20])
print(cn.shape)      # Should print torch.Size([6, 3, 20])