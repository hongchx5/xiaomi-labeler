# devtest-labeler Project

This project is designed to facilitate the labeling of queries using a graphical user interface (GUI). It reads data from a CSV file and allows users to assign labels to each query through button interactions.

## Project Structure

```
devtest-labeler
├── src
│   ├── main.py          # Entry point of the application, initializes the GUI.
│   ├── gui_label.py     # Implements the GUI for displaying queries and rewriting.
│   ├── data_loader.py    # Responsible for reading and parsing the devtest.csv file.
│   └── utils.py         # Contains utility functions, such as saving the updated CSV file.
├── data
│   └── devtest.csv      # The data file to be labeled, containing columns: label, query, query_rewriting.
├── tests
│   └── test_data_loader.py # Unit tests for functions in data_loader.py to ensure correctness.
├── requirements.txt      # Lists the required Python libraries and dependencies.
├── .gitignore            # Specifies files and directories to ignore in version control.
└── README.md             # Documentation and usage instructions for the project.
```

## Usage

1. **Install Dependencies**: Ensure you have Python installed, then install the required libraries listed in `requirements.txt` using:
   ```
   pip install -r requirements.txt
   ```

2. **Prepare Data**: Place your `devtest.csv` file in the `data` directory. Ensure it has the correct format with columns: `label`, `query`, and `query_rewriting`.

3. **Run the Application**: Execute the main application by running:
   ```
   python src/main.py
   ```

4. **Label Queries**: The GUI will display each query along with its rewriting. Use the buttons to assign labels (1, 2, 3, or 4) to the queries. The labels will be saved back to the `devtest.csv` file.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.