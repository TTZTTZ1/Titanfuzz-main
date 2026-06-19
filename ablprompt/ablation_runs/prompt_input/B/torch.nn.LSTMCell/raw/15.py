import torch
from torch.nn import LSTMCell

# Define the dimensions
input_size = 10
hidden_size = 20

# Create an instance of LSTMCell
lstm_cell = LSTMCell(input_size, hidden_size)

# Initialize input and hidden states
input_tensor = torch.randn(5, input_size)  # Batch size of 5, sequence length of 5
hidden_state = torch.zeros(5, hidden_size)
cell_state = torch.zeros(5, hidden_size)

# Process each time step
for i in range(input_tensor.size(0)):
    hidden_state, cell_state = lstm_cell(input_tensor[i], (hidden_state, cell_state))

print("Final Hidden State:", hidden_state)
print("Final Cell State:", cell_state)