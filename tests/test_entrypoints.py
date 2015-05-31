import subprocess


def test_main():
    """The module should be able to be run as a script."""
    subprocess.check_output(['python', '-m', 'moneyme'])


def test_moneyme_entrypoint():
    """The moneyme command should run."""
    subprocess.call(['moneyme'])
