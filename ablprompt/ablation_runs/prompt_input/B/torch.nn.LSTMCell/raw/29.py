import torch
from torch.nn import LSTMCell

# Define model parameters
input_size = 10
hidden_size = 20

# Initialize LSTMCell
lstm_cell = LSTMCell(input_size, hidden_size)

# Create random input and initial hidden/cell states
input_data = torch.randn(5, input_size)  # Sequence length of 5
initial_hidden_state = torch.zeros(5, hidden_size)
initial_cell_state = torch.zeros(5, hidden_size)

# Process the input through the LSTMCell
for i in range(input_data.size(0)):
    hidden_state, cell_state = lstm_cell(input_data[i], (initial_hidden_state[i], initial_cell_state[i]))
    print(f"Time step {i}: Hidden State = {hidden_state}, Cell State = {cell_state}")