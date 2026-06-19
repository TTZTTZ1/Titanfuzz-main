import torch

# Define model parameters
input_size = 10
hidden_size = 20
num_layers = 2
nonlinearity = 'relu'
batch_first = True
dropout = 0.5
bidirectional = False

# Create an instance of RNN
rnn = torch.nn.RNN(input_size, hidden_size, num_layers, nonlinearity=nonlinearity, batch_first=batch_first, dropout=dropout, bidirectional=bidirectional)

# Generate random input data
batch_size = 3
sequence_length = 4
input_data = torch.randn(sequence_length, batch_size, input_size)

# Forward pass through RNN
output, hidden_state = rnn(input_data)

print("Output:", output)
print("Hidden State:", hidden_state)