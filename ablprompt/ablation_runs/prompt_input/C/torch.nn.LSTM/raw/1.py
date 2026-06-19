import torch
from torch.nn import LSTM

# Define model parameters
input_size = 10
hidden_size = 20
num_layers = 2
batch_first = True
dropout = 0.5
bidirectional = True
proj_size = 10

# Create an instance of LSTM
lstm = LSTM(input_size, hidden_size, num_layers, batch_first=batch_first, dropout=dropout, bidirectional=bidirectional, proj_size=proj_size)

# Example input tensor
input_tensor = torch.randn(5, 3, 10)  # (seq_len=5, batch=3, input_size=10)

# Initialize hidden and cell states
h0 = torch.randn(num_layers * (2 if bidirectional else 1), 3, proj_size)  # (num_layers*(2 if bidirectional else 1), batch, proj_size)
c0 = torch.randn(num_layers * (2 if bidirectional else 1), 3, proj_size)  # (num_layers*(2 if bidirectional else 1), batch, proj_size)

# Forward pass through LSTM
output, (hn, cn) = lstm(input_tensor, (h0, c0))

print("Output:", output.shape)
print("Final Hidden State:", hn.shape)
print("Final Cell State:", cn.shape)