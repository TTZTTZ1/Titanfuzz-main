import torch
from torch.nn import LSTM

# Define the LSTM model
lstm = LSTM(input_size=10, hidden_size=20, num_layers=2, batch_first=True, bidirectional=True)

# Create random input tensor
input_tensor = torch.randn(5, 3, 10)

# Initialize hidden and cell states
h0 = torch.randn(4, 3, 20)
c0 = torch.randn(4, 3, 20)

# Forward pass through the LSTM
output, (hn, cn) = lstm(input_tensor, (h0, c0))

print(output.shape)  # Should print: torch.Size([5, 3, 40])
print(hn.shape)      # Should print: torch.Size([4, 3, 20])
print(cn.shape)      # Should print: torch.Size([4, 3, 20])