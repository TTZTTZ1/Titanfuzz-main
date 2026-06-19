import torch
from torch.nn import RNN

# Define the RNN model
input_size = 10
hidden_size = 20
num_layers = 2
rnn = RNN(input_size, hidden_size, num_layers, nonlinearity='tanh', batch_first=True)

# Create some random input data
batch_size = 5
sequence_length = 3
input_data = torch.randn(sequence_length, batch_size, input_size)

# Forward pass through the RNN
output, hidden_state = rnn(input_data)

print(output.shape)
print(hidden_state.shape)