import torch
import torch.nn as nn

# Define the LSTM model
lstm = nn.LSTM(input_size=10, hidden_size=20, num_layers=2, batch_first=True)

# Create random input tensor of shape (sequence_length, batch_size, input_size)
input_tensor = torch.randn(5, 3, 10)

# Initialize hidden and cell states
h0 = torch.zeros(2, 3, 20)
c0 = torch.zeros(2, 3, 20)

# Forward pass through the LSTM
output, (hn, cn) = lstm(input_tensor, (h0, c0))

print("Output:", output.shape)
print("Hidden State:", hn.shape)
print("Cell State:", cn.shape)