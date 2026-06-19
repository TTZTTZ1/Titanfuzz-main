import torch

# Define model parameters
input_size = 10
hidden_size = 20

# Create LSTMCell instance
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Initialize input and hidden/cell states
input_tensor = torch.randn(1, input_size)  # Batch size of 1
hidden_state = torch.zeros(1, hidden_size)
cell_state = torch.zeros(1, hidden_size)

# Forward pass through LSTMCell
next_hidden_state, next_cell_state = lstm_cell(input_tensor, (hidden_state, cell_state))

print("Next Hidden State:", next_hidden_state)
print("Next Cell State:", next_cell_state)