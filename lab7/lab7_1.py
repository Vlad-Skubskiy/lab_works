class GraphicEditor:
    def __init__(self):
        self.history = []
        self.current_state = None

    def make_change(self, change):
        if self.current_state is not None:
            self.history.append(self.current_state)
        self.current_state = change

    def undo(self):
        if not self.history:
            print("not changes for annul")
            return
        self.current_state = self.history.pop()
        print(f"Rolled back to previous state: {self.current_state}")


editor = GraphicEditor()
editor.make_change("Add figure")
editor.make_change("Change color")
editor.make_change("Add text")

editor.undo()
editor.undo()
editor.undo()