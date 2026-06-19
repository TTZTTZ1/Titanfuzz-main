import torch
from torch.nn import LSTM

# Define model parameters
input_size = 10
hidden_size = 20
num_layers = 2
batch_first = True
bidirectional = True
proj_size = 10

# Create an LSTM instance
lstm = LSTM(input_size, hidden_size, num_layers, batch_first=batch_first, bidirectional=bidirectional, proj_size=proj_size)

# Generate random input and initial states
seq_len = 5
batch_size = 3
input_tensor = torch.randn(seq_len, batch_size, input_size)
h0 = torch.randn(num_layers * (2 if bidirectional else 1), batch_size, proj_size if proj_size > 0 else hidden_size)
c0 = torch.randn(num_layers * (2 if bidirectional else 1), batch_size, proj_size if proj_size > 0 else hidden_size)

# Forward pass through the LSTM
output, (hn, cn) = lstm(input_tensor, (h0, c0))

print("Output:", output.shape)
print("Final Hidden State:", hn.shape)
print("Final Cell State:", cn.shape)