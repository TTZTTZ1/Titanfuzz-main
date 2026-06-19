import torch
from torch.nn import LSTM

# Define the LSTM model
input_size = 10
hidden_size = 20
num_layers = 2
lstm = LSTM(input_size, hidden_size, num_layers)

# Create dummy input tensor
sequence_length = 5
batch_size = 3
input_tensor = torch.randn(sequence_length, batch_size, input_size)

# Initialize hidden and cell states
h0 = torch.zeros(num_layers, batch_size, hidden_size)
c0 = torch.zeros(num_layers, batch_size, hidden_size)

# Forward pass through the LSTM
output, (hn, cn) = lstm(input_tensor, (h0, c0))

print("Output:", output.shape)
print("Final hidden state:", hn.shape)
print("Final cell state:", cn.shape)