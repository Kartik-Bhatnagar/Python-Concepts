import math
class Point:
    "Represents a point in two-dimensional geometric coordinates"
    def __init__(self, x=0, y=0):
        """Initialize the position of a new point. The x and y
        coordinates can be specified. If they are not, the
        point defaults to the origin."""
        self.move(x, y)
    def move(self, x, y):
        "Move the point to a new location in 2D space."
        self.x = x
        self.y = y
    def reset(self):
        "Reset the point back to the geometric origin: 0, 0"
        self.move(0, 0)
    def calculate_distance(self, other_point):
        """Calculate the distance from this point to a second
        point passed as a parameter.
        This function uses the Pythagorean Theorem to calculate
        the distance between the two points. The distance is
        returned as a float."""
        return math.sqrt(
        (self.x - other_point.x) ** 2
        + (self.y - other_point.y) ** 2
        )
    
print(help(Point))  

""", it is important to write API documentation that clearly summarizes what each object and method does.
Keeping documentation up to date is difficult; the best way to do it is to write it right into
our code."""
"""Python supports this through the use of docstrings. Each class, function, or method header
can have a standard Python string as the first line following the definition (the line that
ends in a colon). This line should be indented the same as the code that follows it.
Docstrings are simply Python strings enclosed with apostrophes (') or quotation marks (")
characters. Often, docstrings are quite long and span multiple lines (the style guide
suggests that the line length should not exceed 80 characters), which can be formatted as
multi-line strings, enclosed in matching triple apostrophe (''') or triple quote 
characters.
A docstring should clearly and concisely summarize the purpose of the class or method it is
describing. It should explain any parameters whose usage is not immediately obvious, and
is also a good place to include short examples of how to use the API."""