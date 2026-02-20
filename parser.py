import argparse


class Parser:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.args = None

    def add_argument(self, *args):
        self.parser.add_argument(*args, required=True)

    def parse_arguments(self):
        self.args = self.parser.parse_args()
        return self.args
