import torch
from torch.nn import RNN

# Define model parameters
input_size = 10
hidden_size = 20
num_layers = 2
nonlinearity = 'tanh'
batch_first = True
bidirectional = False
dropout = 0.5

# Create an instance of RNN
rnn = RNN(input_size, hidden_size, num_layers, nonlinearity=nonlinearity, batch_first=batch_first, bidirectional=bidirectional, dropout=dropout)

# Prepare input data
batch_size = 3
sequence_length = 4
input_data = torch.randn(sequence_length, batch_size, input_size)

# Forward pass
output, hidden_state = rnn(input_data)

print("Output shape:", output.shape)
print("Hidden state shape:", hidden_state.shape)