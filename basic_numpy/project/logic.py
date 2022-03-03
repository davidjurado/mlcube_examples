"""Logic file"""
import argparse
import yaml
import numpy as np


def evaluate(data, n_top):
    """Select n top elements"""
    result = np.random.choice(data, size=n_top, replace=False)
    return result


def save_results(data, output_path):
    """Save top n numbers to output txt file"""
    np.savetxt(output_path, data.astype(int), fmt='%i', delimiter='\n')


def main():
    """Main function that recieves input parameters and calculate metrics"""

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--data_path",
        type=str,
        required=True,
        help="Text file containing the input data",
    )
    parser.add_argument(
        "--output_file",
        type=str,
        required=True,
        help="file to store top N results",
    )
    parser.add_argument(
        "--parameters_file",
        "--parameters-file",
        type=str,
        required=True,
        help="File containing parameters for evaluation",
    )
    args = parser.parse_args()

    with open(args.parameters_file, "r") as f:
        params = yaml.full_load(f)

    n_top = int(params["n_top"])

    with open(args.data_path) as f:
        data = [int(i) for i in f.readlines()]

    data = np.array(data)

    result = evaluate(data, n_top)
    print(f"Top {n_top} results:")
    print(result)
    save_results(result, args.output_file)


if __name__ == "__main__":
    main()
