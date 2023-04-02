class Visitor:
    def visit_circle(self, circle):
        pass

    def visit_square(self, square):
        pass


class Shape:
    def accept(self, visitor):
        pass


class Circle(Shape):
    def accept(self, visitor):
        visitor.visit_circle(self)


class Square(Shape):
    def accept(self, visitor):
        visitor.visit_square(self)


class DrawVisitor(Visitor):
    def visit_circle(self, circle):
        print("Drawing a circle")

    def visit_square(self, square):
        print("Drawing a square")


class PrintVisitor(Visitor):
    def visit_circle(self, circle):
        print("Printing a circle")

    def visit_square(self, square):
        print("Printing a square")


if __name__ == '__main__':
    shapes = [Circle(), Square()]
    draw_visitor = DrawVisitor()
    print_visitor = PrintVisitor()

    for shape in shapes:
        shape.accept(draw_visitor)

    for shape in shapes:
        shape.accept(print_visitor)
