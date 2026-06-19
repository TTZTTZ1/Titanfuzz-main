import torch

# Define the dimensions
input_size = 10
hidden_size = 20

# Initialize the LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Create random input and initial hidden/cell states
input_data = torch.randn(1, input_size)
hidden_state = torch.randn(1, hidden_size)
cell_state = torch.randn(1, hidden_size)

# Forward pass through the LSTMCell
next_hidden_state, next_cell_state = lstm_cell(input_data, (hidden_state, cell_state))

print("Next Hidden State:", next_hidden_state)
print("Next Cell State:", next_cell_state)