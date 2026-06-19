import torch

# Define input size, hidden size, and number of layers
input_size = 10
hidden_size = 20
num_layers = 3

# Initialize GRUCell
gru_cell = torch.nn.GRUCell(input_size, hidden_size)

# Create random input and initial hidden state
batch_size = 5
sequence_length = 4
input_tensor = torch.randn(sequence_length, batch_size, input_size)
hidden_state = torch.randn(batch_size, hidden_size)

# Process sequence through GRUCell
for t in range(sequence_length):
    hidden_state = gru_cell(input_tensor[t], hidden_state)

print(hidden_state)