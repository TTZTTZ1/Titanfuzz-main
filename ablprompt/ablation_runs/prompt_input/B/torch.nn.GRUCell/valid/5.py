import torch

# Initialize the GRUCell
gru_cell = torch.nn.GRUCell(input_size=10, hidden_size=20)

# Input sequence and initial hidden state
input_seq = torch.randn(5, 3, 10)  # Sequence of 5 timesteps, batch size 3, input size 10
initial_hidden_state = torch.randn(3, 20)  # Batch size 3, hidden size 20

# Process each timestep
hidden_states = []
for i in range(input_seq.size(0)):
    hidden_state = gru_cell(input_seq[i], initial_hidden_state)
    hidden_states.append(hidden_state)
    initial_hidden_state = hidden_state

# Convert list to tensor
final_hidden_states = torch.stack(hidden_states)
print(final_hidden_states.shape)  # Should be (5, 3, 20)