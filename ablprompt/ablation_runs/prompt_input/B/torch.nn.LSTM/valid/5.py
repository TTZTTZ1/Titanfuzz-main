import torch
import torch.nn as nn

# Define an LSTM model with multiple layers, bidirectional processing, and dropout
lstm = nn.LSTM(input_size=10, hidden_size=20, num_layers=2, bidirectional=True, dropout=0.5)

# Create a random input tensor of shape (sequence_length, batch_size, input_size)
input_tensor = torch.randn(5, 3, 10)

# Initialize hidden and cell states
h0 = torch.randn(4, 3, 20)  # 4 = 2*num_layers * bidirectional
c0 = torch.randn(4, 3, 20)

# Forward pass through the LSTM
output, (hn, cn) = lstm(input_tensor, (h0, c0))

print("Output:", output.shape)
print("Final Hidden State:", hn.shape)
print("Final Cell State:", cn.shape)