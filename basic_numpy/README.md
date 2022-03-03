# Basic example

## Project setup

```bash
# Create Python environment and install MLCube Docker runner 
virtualenv -p python3 ./env && source ./env/bin/activate && pip install mlcube-docker
```

## Folder structure

```bash
├── README.md
├── mlcube
│   ├── mlcube.yaml
│   └── workspace
│       ├── data
│       │   └── data.txt
│       ├── parameters.yaml
│       └── result
│           └── result.txt
└── project
    ├── Dockerfile
    ├── logic.py
    ├── mlcube.py
    └── requirements.txt
```

## How to modify this project

You can change each file described above in order to add your own implementation.

### Requirements file

In this file (`requirements.txt`) you can add all the python dependencies needed for running your implementation, these dependencies will be installed during the creation of the docker image, this happens when you run the ```mlcube run ...``` command.

### Dockerfile

You can add or modify any steps inside the file, this comes handy when you need to install some OS dependencies or even when you want to change the base docker image, inside the file you can find some information about the existing steps.

### Parameters file

This is a yaml file (`parameters.yaml`)that contains all extra parameters that aren't files or directories, for example, here you can place all the hyperparameters that you will use for training a model. This file will be passed as an **input parameter** in the MLCube tasks and then it will be read inside the MLCube container.

### MLCube yaml file

In this file (`mlcube.yaml`) you can find the instructions about the docker image and platform that will be used, information about the project (name, description, authors), and also the tasks defined for the project.

In the existing implementation you will find 1 task:

* evaluate:

    This task takes the following parameters:

  * Input parameters:
    * data_path: Folder path containing input data
    * parameters_file: Extra parameters
  * Output parameters:
    * output_path: File path where output result will be stored

    This task takes the input data and the parameters file, perform the selection of the top n values and then save the output result in the output_path.

### MLCube python file

The `mlcube.py` file is the handler file and entrypoint described in the dockerfile, here you can find all the logic related to how to process each MLCube task. If you want to add a new task first you must define it inside the `mlcube.yaml` file with its input and output parameters and then you need to add the logic to handle this new task inside the `mlcube.py` file.

### Logic file

The `logic.py` file contains the main logic of the project, you can modify this file and write your implementation here to perform different tasks, this logic script is called from the `mlcube.py` file and there are other ways to link your implementation and shown in the [MLCube examples repo](https://github.com/mlcommons/mlcube_examples).

## Tasks execution

```bash
# Run evaluate task.
mlcube run --mlcube=mlcube_cpu.yaml --task=evaluate -Pdocker.build_strategy=always
```
