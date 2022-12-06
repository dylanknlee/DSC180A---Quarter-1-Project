# Obtaining the Raw Data

The raw data for this project is obtainable from the website for Stanford's Network Analysis Project (SNAP): http://snap.stanford.edu/higher-order/data.html

- It's important to note that there are two types of datasets: datasets of small size used for testing analysis (listed in the first table), and datasets of much larger magnitude to test the clustering algorithm's scalability (listed in the second table).
- This project can be run on either type of dataset, so it's recommended to at least download one "small" dataset and one "large" dataset of your choice using the links from the corresponding tables.

Once the datasets of your choice is downloaded, extract their compressed zip files and drop the text file containing the edge pairs between nodes into the `data/raw` folder.

# Running the Project

### Executing the project on test data

- To execute the project to run on test data (no raw data needed), in the project root directory, run the command `python run.py test`.
  - This will run the project code on a small subset of data in similar structure to that of the raw text data, first counting the number of motif occurrences to form a motif adjacency matrix and performing spectral clustering to obtain classified communities of nodes.
