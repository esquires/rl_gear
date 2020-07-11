# RL Gear

This project makes setting up new research projects with
[ray](https://docs.ray.io/en/latest/index.html) a bit more turn-key.

## Installation

`rl_gear` is designed to work with ray version 0.8.5 or later
and has been tested with python 3.6.

```bash
    pip install .
```

## Usage

See `tests/test_train_cartpole.py` for a minimal working example.

## Features

### Canonical networks

Common networks such as DQN and IMPALA are implemented in pytorch
as well as a fully connected network that has separate networks
for the value and policy. There is also a helper class to reduce
boilerplate code for feedforward networks. See `torch_models.py`.

### Setting Up Experiments

Import yaml files from other yaml files to adjust a small portion
for a new experiment or save meta data from an experiment (git info,
requirements.txt, etc). See `utils.py` and `rllib_utils.py`)

### Tensorboard Plotting

After running an experiment multiple times, plot it in matplotlib
with transparent percentiles. See `scripts.py` and `utils.py`


## License

BSD-3-Clause
