import torch
from torch.nn import RNN

# Define model parameters
input_size = 10
hidden_size = 20
num_layers = 2
nonlinearity = 'tanh'
bias = True
batch_first = True
dropout = 0.5
bidirectional = False

# Create an instance of RNN
rnn = RNN(input_size, hidden_size, num_layers, nonlinearity, bias, batch_first, dropout, bidirectional)

# Prepare some random input data
batch_size = 3
sequence_length = 4
input_data = torch.randn(sequence_length, batch_size, input_size)

# Forward pass through the RNN
output, hidden_state = rnn(input_data)

print("Output shape:", output.shape)
print("Hidden state shape:", hidden_state.shape)