# Easy JSON Text Format

A very simple text storage format for programmatic manipulation of text. 

The JSON file is a map with the following structure:

```json
{
    styles: [...],
    sections: [...],
    text: [...]
}
```


The styles section contains a list of styles, which are maps of attributes such 
as font size, font format (bold, italics), and color. 

Styles can also reference
other styles and inherit their properties.

e.g.:
```json
{
    id: 1,
    color: "green",
    size: "14px",
    inherits: 2,

}
```

The sections portion contains a sequence of sections. e.g.

```json
{
    id: 1,
    name: "Chapter 1"
},
{
    id: 2,
    name: "Footnotes"
}
```

The text is stored as a JSON file containing a list of text elements. Each text
element consists of a map containing the actual contents of the text, it's stylistic
attributes, and organizational attributes such as the section that it belongs to.
Text could also link to some other portion of text through a link attribute, pointing
at the ID of another text object

```json
{
    id: 1,
    style: 1,
    content: "The quick brown fox jumped over the lazy dog",
    section: 1
},
{
    id: 2,
    style: 1,
    content: "[1]",
    link: 3,
    section: 1
},
{
    id: 3,
    style: 1,
    content: "This is a footnote",
    section: 2
}
```



