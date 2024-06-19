from typing import List


class Task:
    def __init__(self, title: str, description: str):
        self.title = title
        self.description = description

tasks: List[Task] = []
