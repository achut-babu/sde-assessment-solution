# SDE Online Assessment

## Solution Explanation

1. sde_solution.py accepts two arguments.
  a. input file path - file path of the jnput json
  b. output file path - file path where the output json file will be written to
2. Solution logic was to separate the corporate and government bonds and then compare the closeness of each corporate to each government bond and then get the smallest difference to determine the closeness of the two. Once the pairs have been identified, the yield is calculated and stored in output.

3. The time complexity in this case is O(N) i.e. it is of linear time complexity that depends on the number of corporate bonds in the input.

## To run locally

1. python sde_solution.py <input_file_path> <output_file_path>
    ```bash
    python sde_solution.py sample_input.json sample_output.json
    ```

## To run using docker

1. Build docker image.
    ```bash
      docker image build -t sde-solution .
    ```
2. Run the executable in docker by passing input and output files passed as environment variables to the container.
    ```bash
      docker run -v $PWD/:/submission -e INPUT_FILE_PATH=sample_input.json -e OUTPUT_FILE_PATH=sample_output.json sde-solution:latest
    ```
3. To run unit tests.
    ```bash
      docker run -v $PWD/:/submission --entrypoint pytest sde-solution:latest
    ```
