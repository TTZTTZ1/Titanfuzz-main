import torch

# Define the RNN model
input_size = 10
hidden_size = 20
num_layers = 2
rnn = torch.nn.RNN(input_size, hidden_size, num_layers, nonlinearity='relu')

# Create some dummy input data
batch_size = 5
sequence_length = 3
input_data = torch.randn(sequence_length, batch_size, input_size)

# Initialize hidden state
h0 = torch.zeros(num_layers, batch_size, hidden_size)

# Forward pass through RNN
output, hn = rnn(input_data, h0)

print("Output:", output)
print("Hidden State:", hn)