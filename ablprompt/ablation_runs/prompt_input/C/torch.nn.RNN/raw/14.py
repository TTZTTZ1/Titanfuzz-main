import torch

# Define the RNN model
rnn = torch.nn.RNN(input_size=10, hidden_size=20, num_layers=2, nonlinearity='relu', batch_first=True, bidirectional=True)

# Create some random input data
input_data = torch.randn(5, 3, 10)  # sequence length, batch size, input size

# Initialize the hidden state
h_0 = torch.zeros(4, 3, 20)  # (num_layers * num_directions, batch_size, hidden_size)

# Forward pass through the RNN
output, h_n = rnn(input_data, h_0)

print(output.shape)  # Should be (5, 3, 40)
print(h_n.shape)   # Should be (4, 3, 20)