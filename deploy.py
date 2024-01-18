import argparse, subprocess, git, os, logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_software(software):
    try:
        subprocess.run(f"{software} --version", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f"{software} is not installed. Please install {software} to deploy")
        return False


def generate_branch_name(base_name):
    timestamp = datetime.now().strftime("%Y-%m-%d-%H")
    return f"{base_name}_{timestamp}"

def deploy(dev=False, test=False, acc=False, prod=False, done=False, dir="./To-do"):
    if dev:
        if done:
            if check_software("docker"):
                try:
                    subprocess.run(f"docker-compose -f {dir}/docker-compose.dev.yml up --build -d", shell=True, check=True)
                    print(f"You can now access the app on the localhost at the provided port, the default is: 0.0.0.0:5000\n when you are done you can shut down docker using \"docker-compose -f {dir}/docker-compose.dev.yml down\" from the current directory or run \"docker ps\" to see all running containers")
                    exit()
                except subprocess.CalledProcessError as e:
                    print(f"While trying to build or run the docker image you encountered this error\n{e.returncode}")
            else:
                exit()
        print("Preparing Dev environment...")
        try:
            os.mkdir(dir)
            print(f"Made dir {dir}")
        except Exception as e:
            logger.error("An unexpected error occurred")

        repo_clone_url = 'https://github.com/samoshi/To-do.git'
        repo = git.Repo.clone_from(repo_clone_url, dir)
        repo.git.checkout('-b', generate_branch_name("dev"))
        print(f"Dev environment is complete, you can now find it at {dir}")
    if test:
        if done:
            if check_software("docker"):
                try:
                    subprocess.run(f"docker-compose -f {dir}/docker-compose.test.yml up --build -d", shell=True, check=True)
                    print(f"You can now access the app on the localhost at the provided port, the default is: 0.0.0.0:5000\n when you are done you can shut down docker using \"docker-compose -f {dir}/docker-compose.test.yml down\" from the current directory or run \"docker ps\" to see all running containers")
                    exit()
                except subprocess.CalledProcessError as e:
                    print(f"While trying to build or run the docker image you encountered this error\n{e.returncode}")
            else:
                exit()
        print("Preparing Test environment...")
        try:
            os.mkdir(dir)
            print(f"Made dir {dir}")
        except Exception as e:
            logger.error("An unexpected error occurred")

        repo_clone_url = 'https://github.com/samoshi/To-do.git'
        repo = git.Repo.clone_from(repo_clone_url, dir)
        repo.git.checkout('-b', generate_branch_name("test"))
        print(f"Test environment is complete, you can now find it at {dir}")
    if acc:
        if done:
            if check_software("docker") and check_software("gcloud") and check_software("kubectl"):
                try:
                    subprocess.run(f"docker-compose -f {dir}/docker-compose.acc.yml build", shell=True, check=True)
                    subprocess.run(f"docker-compose -f {dir}/docker-compose.acc.yml push", shell=True, check=True)
                    # There was a function to update the yml with the new image, however that was malfunctioning and I removed it, instead this should be done manually
                    # subprocess.run(f"kubectl apply -f {dir}/acc-deployment.yml --force", shell=True, check=True)
                    # print("exposing kubernetes deployment with port 80")
                    # subprocess.run("kubectl expose deployment to-do-app-acc --type=LoadBalancer --port=80 --target-port=80", shell=True, check=True)
                    # print("You can now access the app as soon as you see the ip provided by k8s by running \"kubectl get deployments\" and/or \"kubectl get services\"")
                    exit()
                except subprocess.CalledProcessError as e:
                    print("While trying to deploy the docker image you encountered an error")
                    exit()
            else:
                exit()
        print("Preparing Acceptance environment...")
        try:
            os.mkdir(dir)
            print(f"Made dir {dir}")
        except Exception as e:
            logger.error("An unexpected error occurred")

        repo_clone_url = 'https://github.com/samoshi/To-do.git'
        repo = git.Repo.clone_from(repo_clone_url, dir)
        repo.git.checkout('-b', generate_branch_name("Acceptance"))
        print(f"Acceptance environment is complete, you can now find it at {dir}")
    if prod:
        if done:
            if check_software("docker") and check_software("gcloud") and check_software("kubectl"):
                try:
                    subprocess.run(f"docker-compose -f {dir}/docker-compose.acc.yml build", shell=True, check=True)
                    subprocess.run(f"docker-compose -f {dir}/docker-compose.acc.yml push", shell=True, check=True)
                    # There was a function to update the yml with the new image, however that was malfunctioning and I removed it, instead this should be done manually
                    # subprocess.run(f"kubectl apply -f {dir}/acc-deployment.yml --force", shell=True, check=True)
                    # print("exposing kubernetes deployment with port 80")
                    # subprocess.run("kubectl expose deployment to-do-app--type=LoadBalancer --port=80 --target-port=80", shell=True, check=True)
                    # print("You can now access the app as soon as you see the ip provided by k8s by running \"kubectl get deployments\" and/or \"kubectl get services\"")
                    exit()
                except subprocess.CalledProcessError as e:
                    print("While trying to deploy the docker image you encountered an error")
                    exit()
            else:
                exit()
        print("Preparing Production environment...")
        try:
            os.mkdir(dir)
            print(f"Made dir {dir}")
        except Exception as e:
            logger.error("An unexpected error occurred")

        repo_clone_url = 'https://github.com/samoshi/To-do.git'
        repo = git.Repo.clone_from(repo_clone_url, dir)
        print(f"Production environment is complete, you can now find it at {dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Tiered Development and Deployment Script")
    parser.add_argument("--dev", action="store_true", help="Setup a Development environment")
    parser.add_argument("--test", action="store_true", help="Setup a Testing environment")
    parser.add_argument("--acc", action="store_true", help="Setup an Acceptance environment")
    parser.add_argument("--prod", action="store_true", help="Setup a Production environment")
    parser.add_argument("--done", action="store_true", help="Deploy to the selected environment\n Example usage: python deploy.py --dev --done")
    parser.add_argument("--dir", action="store", help="Select a directory to clone the git repo (Default is ./To-do)\n Example usage: python deploy.py --dev --dir=./path/to/directory/")

    args = parser.parse_args()

    if not any([args.dev, args.test, args.acc, args.prod]):
        parser.error("Please select at least one environment to deploy.")
    
    directory = args.dir or "./To-do"
    deploy(dev=args.dev, test=args.test, acc=args.acc, prod=args.prod, done=args.done, dir=directory)
