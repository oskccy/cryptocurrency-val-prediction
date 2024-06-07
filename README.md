# Cryptocurrency val prediction
> By: Oscar
## Index

1. [Introduction](#introduction)
2. [Requirements Installation](#requirements-installation)
3. [Project Structure](#project-structure)
4. [Usage Instructions](#usage-instructions)
5. [Customization](#customization)
6. [Contributions](#contributions)

## Introduction

> This project demonstrates historical predictions of the price of a cryptocurrency against an "against currency" using a multi-layered LSTM neural network. The project is heavily modular, with different components for data loading, preprocessing, model building, training, prediction, and plotting. Plotting is done dynamically for visualization aid of predictions.

> Furthermore, percent error is calculated throughout each prediction value, based on the prediction data, and the real ticker data.

## Requirements Installation

To get started with this project, you need to install the required packages. Follow the steps below:

1. **Create a virtual environment (optional but recommended)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scriptsctivate`
    ```

2. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

## Project Structure

> within architecture

- `data_loader.py`: Module for loading and preprocessing data.
- `model_builder.py`: Module for building and compiling the model.
- `trainer.py`: Module for training the model.
- `predictor.py`: Module for testing and making predictions.
- `plotter.py`: Module for plotting the results.
- `run.py`: The main script that ties everything together.

## Usage Instructions

1. **Clone the repository**:
    ```bash
    git clone https://github.com/oskccy/cryptocurrency-val-prediction.git
    cd predictor
    ```

2. **Run the project**:
    ```bash
    python run.py
    ```

## Customization
> You can customize the cryptocurrency and fiat currency pair by changing the `crypto` and `against` variables directly in the console. Make sure it's a real crypto ticker and against currency.

## Contributions

> contributing to this project would mean the world to me. *make this better*, ***sumbit pull requests***, because *im not a genius*. thank you so much!

