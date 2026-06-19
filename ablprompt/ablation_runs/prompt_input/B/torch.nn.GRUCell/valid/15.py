import torch
from torch.nn import GRUCell

# Define the input size, hidden size, and number of time steps
input_size = 10
hidden_size = 20
num_time_steps = 5

# Initialize the GRUCell
gru_cell = GRUCell(input_size, hidden_size)

# Create random input tensor and initial hidden state
input_tensor = torch.randn(num_time_steps, input_size)
initial_hidden_state = torch.randn(hidden_size)

# Process the input sequence through the GRUCell
current_hidden_state = initial_hidden_state
for t in range(num_time_steps):
    current_hidden_state = gru_cell(input_tensor[t], current_hidden_state)

print("Final Hidden State:", current_hidden_state)