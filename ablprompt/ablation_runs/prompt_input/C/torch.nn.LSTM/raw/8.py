import torch
import torch.nn as nn

# Define the LSTM model
input_size = 10
hidden_size = 20
num_layers = 2
lstm = nn.LSTM(input_size, hidden_size, num_layers)

# Prepare the input sequence
batch_size = 3
sequence_length = 5
input_seq = torch.randn(sequence_length, batch_size, input_size)

# Forward pass through the LSTM
output, (hn, cn) = lstm(input_seq)

print("Output:", output.shape)
print("Final Hidden State:", hn.shape)
print("Final Cell State:", cn.shape)