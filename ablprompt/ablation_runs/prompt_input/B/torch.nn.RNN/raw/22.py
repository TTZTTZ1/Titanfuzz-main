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

# Initialize hidden state
if bidirectional:
    hx = torch.randn(2 * num_layers, batch_size, hidden_size)
else:
    hx = torch.randn(num_layers, batch_size, hidden_size)

# Forward pass through RNN
output, hn = rnn(input_data, hx)

print("Output:", output)
print("Final Hidden State:", hn)