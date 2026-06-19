import torch
from torch.nn import LSTMCell

# Define model parameters
input_size = 10
hidden_size = 20

# Initialize LSTMCell
lstm_cell = LSTMCell(input_size, hidden_size)

# Create random input and initial states
input_tensor = torch.randn(5, input_size)  # Batch size of 5, sequence length of 5
hidden_state = torch.zeros(5, hidden_size)
cell_state = torch.zeros(5, hidden_size)

# Forward pass through LSTMCell
next_hidden_state, next_cell_state = lstm_cell(input_tensor, (hidden_state, cell_state))

print("Next Hidden State:", next_hidden_state)
print("Next Cell State:", next_cell_state)