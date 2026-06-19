import torch
from torch.nn import RNN

# Define model parameters
input_size = 10
hidden_size = 20
num_layers = 2
nonlinearity = 'relu'
batch_first = True
dropout = 0.5
bidirectional = False

# Create an instance of RNN
rnn = RNN(input_size, hidden_size, num_layers, nonlinearity=nonlinearity, batch_first=batch_first, dropout=dropout, bidirectional=bidirectional)

# Prepare input data
batch_size = 32
sequence_length = 50
input_data = torch.randn(sequence_length, batch_size, input_size)

# Forward pass through RNN
output, hidden_state = rnn(input_data)

print("Output shape:", output.shape)
print("Hidden state shape:", hidden_state.shape)