import torch
from torch.nn import LSTMCell

# Initialize LSTMCell
lstm_cell = LSTMCell(input_size=10, hidden_size=20)

# Input data
input_data = torch.randn(5, 3, 10)  # seq_len x batch_size x input_size
initial_hidden_state = torch.zeros(3, 20)  # batch_size x hidden_size
initial_cell_state = torch.zeros(3, 20)   # batch_size x hidden_size

# Process each time step
hidden_states = []
cell_states = []

for i in range(input_data.size(0)):
    hidden_state, cell_state = lstm_cell(input_data[i], (initial_hidden_state, initial_cell_state))
    hidden_states.append(hidden_state)
    cell_states.append(cell_state)

# Convert lists to tensors
hidden_states = torch.stack(hidden_states, dim=0)
cell_states = torch.stack(cell_states, dim=0)

print("Hidden States:", hidden_states.shape)
print("Cell States:", cell_states.shape)