"""
Versehe Objekte dynamisch mit zusätzlichen Funktionen ohne ihre Klasse zu verändern.
Beispiel: Füge einem Textobjekt eine Rahmen- oder Scrollfunktion hinzu.
"""
# ===== Basis-Komponente =====
class Text:
    def __init__(self, content):
        self.content = content

    def render(self):
        return self.content
    
# ===== Decorator-Basis =====
class TextDecorator(Text):
    def __init__(self, wrapped_text):
        self.wrapped_text = wrapped_text

    def render(self):
        return self.wrapped_text.render()


# ===== Konkrete Decorators =====
class BoldDecorator(TextDecorator):
    def render(self):
        return f"<b>{self.wrapped_text.render()}</b>"


class ItalicDecorator(TextDecorator):
    def render(self):
        return f"<i>{self.wrapped_text.render()}</i>"


class UnderlineDecorator(TextDecorator):
    def render(self):
        return f"<u>{self.wrapped_text.render()}</u>"
    
# ===== Beispielverwendung =====
if __name__ == "__main__":
    simple_text = Text("Hello, World!")
    print("Einfacher Text:", simple_text.render()) # Einfacher Text: Hello, World!

    bold_text = BoldDecorator(simple_text)
    print("Fetter Text:", bold_text.render()) # Fetter Text: <b>Hello, World!</b>

    italic_bold_text = ItalicDecorator(bold_text)
    print("Kursiv und Fetter Text:", italic_bold_text.render()) # Kursiv und Fetter Text: <i><b>Hello, World!</b></i>

    underlined_italic_bold_text = UnderlineDecorator(italic_bold_text)
    print("Unterstrichener, Kursiver und Fetter Text:", underlined_italic_bold_text.render()) # Unterstrichener, Kursiver und Fetter Text: <u><i><b>Hello, World!</b></i></u>