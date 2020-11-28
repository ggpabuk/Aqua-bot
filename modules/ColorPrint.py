import sys

def fail(message, prefix = "Error"):
    sys.stderr.write(f"[\u001b[31m{prefix}\x1b[0m] \u001b[31m{message.strip()}\x1b[0m\n")

def warn(message, prefix = "Warning"):
    sys.stderr.write(f"[\u001b[33m{prefix}\x1b[0m] \u001b[33m{message.strip()}\x1b[0m\n")

def blue(message, prefix = "Message"):
    sys.stderr.write(f"[\u001b[34m{prefix}\x1b[0m] \u001b[34m{message.strip()}\x1b[0m\n")

bluecolor = "\u001b[34m"
reset = "\x1b[0m"
