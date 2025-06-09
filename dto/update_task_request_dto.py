
class UpdateTaskRequestDto:
    def __init__(self, content: str,  completed: bool = False):
        self.content = content
        self.completed = completed
        
    def __repr__(self):
        return f"UpdateTaskRequestDto(content={self.content}, completed={self.completed})"