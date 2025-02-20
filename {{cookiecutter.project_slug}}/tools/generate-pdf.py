#!/usr/bin/env python3
import os
import subprocess


def main(report_file):
    """
    This script combines three Markdown files (1-intro.md, 2-results.md, 3-conclusion.md)
    into a single file named '{{ cookiecutter.project_slug }}.md' under the 'report' directory,
    and then converts the combined file to a PDF using the docker-based pandoc/extra image
    and the Eisvogel LaTeX template.
    """

    # The report directory where the final .md and .pdf will go
    report_dir = "report"
    os.makedirs(report_dir, exist_ok=True)

    # The combined Markdown filename (and PDF filename) is based on the cookiecutter project_slug
    project_slug = "{{ cookiecutter.project_slug }}"
    combined_md = os.path.join(report_dir, f"{project_slug}.md")
    combined_pdf = os.path.join(report_dir, f"{project_slug}.pdf")

    # Remove any existing combined Markdown file (to start fresh)
    if os.path.exists(combined_md):
        os.remove(combined_md)

    # List the input files in the order you want to append
    # Combine the files into one Markdown
    with open(combined_md, "a", encoding="utf-8") as out_file:
        if os.path.isfile(report_file):
            with open(report_file, "r", encoding="utf-8") as in_file:
                out_file.write(in_file.read())
        else:
            print(f"Warning: '{report_file}' not found.")

    # Use Docker to run pandoc with the Eisvogel template
    docker_cmd = [
        "docker",
        "run",
        "--rm",
        # Mount the current directory so Docker sees your files
        "-v",
        f"{os.getcwd()}:/data",
        # Run as the current user, so the generated file is owned by you, not root
        "-u",
        f"{os.getuid()}:{os.getgid()}",
        "my-pandoc-extra",  # The Docker image
        combined_md,  # Input file
        "-f",
        "markdown",
        "--listings",
        "--template",
        "eisvogel",  # Make sure this template is included in pandoc/extra (it usually is)
        "--filter",
        "pandoc-latex-environment",
        "-o",
        combined_pdf,
    ]

    # Run the Docker-based pandoc command
    try:
        subprocess.run(docker_cmd, check=True)
        print(f"Successfully generated PDF via Docker: {combined_pdf}")
    except FileNotFoundError:
        print(
            "Error: Docker not found. Make sure Docker is installed and on your system's PATH."
        )
    except subprocess.CalledProcessError as e:
        print(f"Docker-based Pandoc failed with exit code {e.returncode}: {e}")


if __name__ == "__main__":
    report_file = "report.md"
    main(report_file)
