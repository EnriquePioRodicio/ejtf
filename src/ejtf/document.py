from dataclasses import dataclass, field, asdict
from typing import List
import json
from pathlib import Path

from .style import Style
from .section import Section
from .text import Text


@dataclass
class Document:
    styles: List[Style] = field(default_factory=list)
    sections: List[Section] = field(default_factory=list)
    text: List[Text] = field(default_factory=list)

    def add_style(self, color: str = None, size: str = None, inherits: int = None) -> Style:
        """Add a new style with an auto-incremented ID."""
        next_id = max([s.id for s in self.styles], default=0) + 1
        style = Style(id=next_id, color=color, size=size, inherits=inherits)
        self.styles.append(style)
        return style

    def add_section(self, name: str) -> Section:
        """Add a new section with an auto-incremented ID."""
        next_id = max([s.id for s in self.sections], default=0) + 1
        section = Section(id=next_id, name=name)
        self.sections.append(section)
        return section

    def add_text(self, style: int, content: str, section: int, link: int = None) -> Text:
        """Add a new text element with an auto-incremented ID."""
        next_id = max([t.id for t in self.text], default=0) + 1
        text = Text(id=next_id, style=style, content=content, section=section, link=link)
        self.text.append(text)
        return text

    def remove_style(self, style_id: int) -> None:
        """Remove a style and decrement all subsequent IDs."""
        # Remove the style
        self.styles = [s for s in self.styles if s.id != style_id]

        # Decrement IDs greater than the removed ID
        for style in self.styles:
            if style.id > style_id:
                style.id -= 1
            # Update inherits references
            if style.inherits is not None and style.inherits > style_id:
                style.inherits -= 1

        # Update style references in text elements
        for text in self.text:
            if text.style > style_id:
                text.style -= 1

    def remove_section(self, section_id: int) -> None:
        """Remove a section and decrement all subsequent IDs."""
        # Remove the section
        self.sections = [s for s in self.sections if s.id != section_id]

        # Decrement IDs greater than the removed ID
        for section in self.sections:
            if section.id > section_id:
                section.id -= 1

        # Update section references in text elements
        for text in self.text:
            if text.section > section_id:
                text.section -= 1

    def remove_text(self, text_id: int) -> None:
        """Remove a text element and decrement all subsequent IDs."""
        # Remove the text
        self.text = [t for t in self.text if t.id != text_id]

        # Decrement IDs greater than the removed ID
        for text in self.text:
            if text.id > text_id:
                text.id -= 1
            # Update link references
            if text.link is not None and text.link > text_id:
                text.link -= 1

    def save(self, filepath: str) -> None:
        """Save the document to a JSON file."""
        data = {
            "styles": [asdict(style) for style in self.styles],
            "sections": [asdict(section) for section in self.sections],
            "text": [asdict(text) for text in self.text]
        }

        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)

    @classmethod
    def load(cls, filepath: str) -> 'Document':
        """Load a document from a JSON file."""
        with open(filepath, 'r') as f:
            data = json.load(f)

        styles = [Style(**style_data) for style_data in data.get("styles", [])]
        sections = [Section(**section_data) for section_data in data.get("sections", [])]
        text = [Text(**text_data) for text_data in data.get("text", [])]

        return cls(styles=styles, sections=sections, text=text)
