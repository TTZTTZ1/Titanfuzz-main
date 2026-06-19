import torch

# Define input size, hidden size, and number of steps
input_size = 10
hidden_size = 20
num_steps = 5

# Initialize input sequence and initial hidden state
input_seq = torch.randn(num_steps, 1, input_size)
initial_hidden_state = torch.randn(1, 1, hidden_size)

# Create a GRUCell instance
gru_cell = torch.nn.GRUCell(input_size, hidden_size)

# Process each time step in the sequence
current_hidden_state = initial_hidden_state
for i in range(num_steps):
    current_hidden_state = gru_cell(input_seq[i], current_hidden_state)

print("Final Hidden State:", current_hidden_state)