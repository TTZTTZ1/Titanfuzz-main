import torch

# Define the input size, hidden size, and number of time steps
input_size = 10
hidden_size = 20
num_time_steps = 5

# Initialize the input sequence and hidden state
input_sequence = torch.randn(num_time_steps, 1, input_size)
initial_hidden_state = torch.randn(1, 1, hidden_size)

# Create an instance of GRUCell
gru_cell = torch.nn.GRUCell(input_size, hidden_size)

# Process each time step
current_hidden_state = initial_hidden_state
for t in range(num_time_steps):
    current_hidden_state = gru_cell(input_sequence[t], current_hidden_state)

print("Final Hidden State:", current_hidden_state)