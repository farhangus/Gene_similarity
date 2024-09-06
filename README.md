
# Gene Similarity Package

## Overview

The **Gene Similarity** package is a tool designed to calculate the similarities between a set of genes based on their sequences. It computes a similarity matrix using k-mer comparison and generates both a log file with detailed analysis and a heatmap that visually represents the similarity between gene sequences.

## Features
- Parse gene sequences from a file
- Calculate gene similarity using k-mer analysis
- Generate a similarity matrix
- Log results and analysis to a specified log file
- Generate a heatmap representing gene similarity
- Save output files in user-defined directories

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/username/gene_similarity.git
    cd gene_similarity
    ```

2. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

You can run the tool using the command-line interface.

### Example Command:

```bash
python -m gene_similarity -f <path_to_genome_file> -l <output_log_directory> -h <heatmap_filename>
```

### Parameters:

- `-f, --file`: **(Required)** The path to the genome file containing the gene sequences.
- `-k, --kmer-size`: **(Optional)** The k-mer size used for gene comparison. Default is 25.
- `-l, --logger_path`: **(Optional)** The path to the log file or directory where the logs will be saved. If a directory is provided, a default `example.log` file will be created inside. Default is `example.log` in the current directory.
- `-h, --heatmap_path`: **(Optional)** The name of the heatmap image file. The heatmap will be saved in the same directory as the log file unless otherwise specified. Default is `heatmap.png`.

### Options:

- **File**: You must provide the file containing the gene sequences using the `-f` option.
- **Log file**: The `-l` option allows you to specify a directory for the log file or a full log file path. If a directory is specified, the log will be saved as `example.log`.
- **Heatmap**: The `-h` option allows you to specify the heatmap filename. The heatmap will be saved as `heatmap.png` in the specified output directory.

### Example:

```bash
python -m gene_similarity -f sample_genes_2.fa -l output_dir -h gene_similarity_heatmap.png
```

In this example:
- `sample_genes_2.fa`: The file with the gene sequences.
- `output_dir`: The directory where the log and heatmap will be saved.
- `gene_similarity_heatmap.png`: The output heatmap filename.

### Output:

1. **Log File**:
    - A log file containing detailed information about the gene comparison and k-mer analysis is generated in the directory specified by `-l`.

2. **Heatmap**:
    - A heatmap visualizing the gene similarity is generated and saved as a `.png` file in the directory specified by `-h`.

## Dependencies

Make sure you have the following Python packages installed:
- `seaborn`
- `matplotlib`
- `pandas`
- `click`

You can install them using the following command:

```bash
pip install seaborn matplotlib pandas click
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
