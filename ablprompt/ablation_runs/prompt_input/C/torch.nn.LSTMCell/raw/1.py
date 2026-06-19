import torch

# Define the input size, hidden size, and number of time steps
input_size = 10
hidden_size = 20
num_steps = 5

# Initialize the input data and hidden/cell states
input_data = torch.randn(num_steps, 32, input_size)  # Batch size of 32
initial_hidden_state = torch.zeros(32, hidden_size)
initial_cell_state = torch.zeros(32, hidden_size)

# Create an instance of LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Iterate over each time step and update the hidden and cell states
for i in range(num_steps):
    hidden_state, cell_state = lstm_cell(input_data[i], (initial_hidden_state, initial_cell_state))
    initial_hidden_state = hidden_state
    initial_cell_state = cell_state

print("Final Hidden State:", hidden_state)
print("Final Cell State:", cell_state)