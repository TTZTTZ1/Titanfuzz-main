import torch

# Define the RNN model
input_size = 10
hidden_size = 20
num_layers = 2
nonlinearity = 'relu'
batch_first = True
dropout = 0.5
bidirectional = False

rnn = torch.nn.RNN(input_size, hidden_size, num_layers, nonlinearity=nonlinearity, batch_first=batch_first, dropout=dropout, bidirectional=bidirectional)

# Create a random input tensor
batch_size = 3
sequence_length = 4
input_tensor = torch.randn(sequence_length, batch_size, input_size)

# Forward pass through the RNN
output, h_n = rnn(input_tensor)

print("Output:", output)
print("Final Hidden State:", h_n)