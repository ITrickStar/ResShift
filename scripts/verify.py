import subprocess
import yaml

def check_dependencies_requirements(requirements_file):
    try:
        with open(requirements_file, "r") as file:
            dependencies = [line.strip() for line in file]

        missing_dependencies = []
        for dependency in dependencies:
            try:
                __import__(dependency)
            except ImportError:
                missing_dependencies.append(dependency)

        return missing_dependencies

    except FileNotFoundError:
        print(f"File {requirements_file} not found")
        return None


def read_yaml(file_path):
    with open(file_path, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            return None


def check_dependencies_yaml(yaml_file):
    yalm_source = read_yaml(yaml_file)
    if yalm_source is None:
        print("There are no dependencies.")
        return

    dependencies = yalm_source["dependencies"]
    pip_dependencies = dependencies[98]["pip"]
    missing_dependencies = []
    for dep in pip_dependencies:
        package_name = dep
        if dep.find("<") != -1:
            package_name = dep[: dep.find("<")].strip()
        elif dep.find(">") != -1:
            package_name = dep[: dep.find(">")].strip()
        elif dep.find("=") != -1:
            package_name = dep[: dep.find("=")].strip()
        elif dep.find("@") != -1:
            package_name = dep[: dep.find("@")].strip()
        try:
            subprocess.check_output(["pip", "show", package_name])
        except subprocess.CalledProcessError:
            missing_dependencies.append(package_name)
            print(package_name, "is NOT installed.")
        print(package_name, "CHECKED")

    if missing_dependencies:
        print("\x1b[31m" + "Missing dependencies:")
        for dep in missing_dependencies:
            print(dep)
    else:
        print("\x1b[32m" + "Everything is OK!")
    print("\x1b[0m")


if __name__ == "__main__":
    yaml_file = "environment.yml"
    requirements_file = "requirements.txt"
    check_dependencies_requirements(requirements_file)
    check_dependencies_yaml(yaml_file)
