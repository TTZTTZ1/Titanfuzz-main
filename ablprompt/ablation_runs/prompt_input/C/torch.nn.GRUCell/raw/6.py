import torch
import torch.nn as nn

# Define the input size, hidden size, and number of layers
input_size = 10
hidden_size = 20
num_layers = 2

# Create a random input sequence and initial hidden state
batch_size = 5
sequence_length = 3
input_seq = torch.randn(sequence_length, batch_size, input_size)
h0 = torch.randn(num_layers, batch_size, hidden_size)

# Initialize the GRUCell
gru_cell = nn.GRUCell(input_size, hidden_size)

# Process each time step in the sequence
for t in range(sequence_length):
    h0 = gru_cell(input_seq[t], h0)

print(h0.shape)  # Output should be (num_layers, batch_size, hidden_size)