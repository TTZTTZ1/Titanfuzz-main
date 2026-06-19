import torch

# Define input size, hidden size, and number of layers
input_size = 10
hidden_size = 20
num_layers = 3

# Create a dummy input sequence and initial hidden state
batch_size = 5
sequence_length = 4
dummy_input = torch.randn(sequence_length, batch_size, input_size)
initial_hidden_state = torch.randn(num_layers, batch_size, hidden_size)

# Initialize the GRUCell
gru_cell = torch.nn.GRUCell(input_size, hidden_size)

# Forward pass through the GRUCell
for t in range(sequence_length):
    hidden_state = gru_cell(dummy_input[t], initial_hidden_state)
    print(f"Hidden State at time {t}: {hidden_state}")