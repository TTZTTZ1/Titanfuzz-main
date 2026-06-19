import torch
import torch.nn as nn

# Define the LSTM model
lstm = nn.LSTM(input_size=10, hidden_size=20, num_layers=2, batch_first=True)

# Create random input tensor
input_tensor = torch.randn(5, 3, 10)  # (sequence_length, batch_size, input_size)

# Initialize hidden and cell states
h0 = torch.randn(2, 3, 20)  # (num_layers, batch_size, hidden_size)
c0 = torch.randn(2, 3, 20)

# Forward pass through the LSTM
output, (hn, cn) = lstm(input_tensor, (h0, c0))

print("Output:", output)
print("Final Hidden State:", hn)
print("Final Cell State:", cn)