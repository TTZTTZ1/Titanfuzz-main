import torch
from torch.nn import RNN

# Define model parameters
input_size = 10
hidden_size = 20
num_layers = 2
nonlinearity = 'relu'
batch_first = True
bidirectional = True
dropout = 0.5

# Create an instance of the RNN model
rnn = RNN(input_size, hidden_size, num_layers, nonlinearity=nonlinearity, batch_first=batch_first, bidirectional=bidirectional, dropout=dropout)

# Prepare some random input data
batch_size = 3
sequence_length = 4
input_data = torch.randn(sequence_length, batch_size, input_size)

# Forward pass through the RNN
output, hidden_state = rnn(input_data)

print("Output:", output)
print("Hidden State:", hidden_state)