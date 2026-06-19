import torch

# Define the model parameters
input_size = 10
hidden_size = 20
num_layers = 2
nonlinearity = 'tanh'
bias = True
batch_first = True
dropout = 0.5
bidirectional = False

# Create the RNN model
rnn_model = torch.nn.RNN(input_size=input_size,
                         hidden_size=hidden_size,
                         num_layers=num_layers,
                         nonlinearity=nonlinearity,
                         bias=bias,
                         batch_first=batch_first,
                         dropout=dropout,
                         bidirectional=bidirectional)

# Example input sequence
batch_size = 3
sequence_length = 4
input_sequence = torch.randn(sequence_length, batch_size, input_size)

# Forward pass through the RNN
output, hidden_state = rnn_model(input_sequence)

print("Output:", output)
print("Hidden State:", hidden_state)