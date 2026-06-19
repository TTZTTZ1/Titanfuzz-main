import torch

# Define the input size, hidden size, and number of time steps
input_size = 10
hidden_size = 20
num_time_steps = 5

# Create a random input sequence and initial hidden state
input_sequence = torch.randn(num_time_steps, 1, input_size)
initial_hidden_state = torch.randn(1, 1, hidden_size)

# Initialize the GRUCell
gru_cell = torch.nn.GRUCell(input_size, hidden_size)

# Process each time step
hidden_states = []
for t in range(num_time_steps):
    current_input = input_sequence[t]
    if t == 0:
        current_hidden_state = initial_hidden_state
    else:
        current_hidden_state = hidden_states[-1]
    next_hidden_state = gru_cell(current_input, current_hidden_state)
    hidden_states.append(next_hidden_state)

# Output the final hidden state
final_hidden_state = hidden_states[-1]
print(final_hidden_state)