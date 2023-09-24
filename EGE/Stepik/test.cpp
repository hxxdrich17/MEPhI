#include <iostream>
#include <cmath>

class Point;
class Figure;
class Circle;
class Rectangle;
class UnitedFigure;
class ComplementedFigure;
class IntersectedFigure;

class Point {
public:
   double x;
   double y;
   Point() = default;
   Point(double _x, double _y) : x(_x), y(_y) {}
   Point operator + (const Point& p) const {
       return Point {x + p.x, y + p.y};
   }
   Point operator - (const Point& p) const {
       return Point {x - p.x, y - p.y};
   }
   static Point max (const Point& p1, const Point& p2) {
       return Point {std::max(p1.x, p2.x), std::max(p1.y, p2.y)};
   }
   static Point min (const Point& p1, const Point& p2) {
       return Point {std::min(p1.x, p2.x), std::min(p1.y, p2.y)};
   }
   double vec_length () const {
       return sqrt(x*x + y*y);
   }
};

class Figure {
public:
   virtual double distance_to (const Point &p) const = 0;
   friend UnitedFigure operator + (const Figure & f1, const Figure & f2);
   friend ComplementedFigure operator - (const Figure & f1, const Figure & f2);
   friend IntersectedFigure operator & (const Figure & f1, const Figure & f2);
   bool is_point_into(const Point &p) const {
       return distance_to(p) <= 0;
   }
};

class Circle : public Figure {
   Point o;
   double r;
public:
   Circle (Point p, double _r) : o(p), r(_r) {}
   double distance_to (const Point &p) const override {
       return (o - p).vec_length() - r;
   }
};

class Rectangle : public Figure {
   Point a;
   Point b;
public:
   Rectangle (Point p1, Point p2) : a(Point::min(p1, p2)), b(Point::max(p1, p2)) {}
   double distance_to (const Point &p) const override {
       auto d = Point::max(a - p, p - b);
       return Point::max(d, Point {0, 0}).vec_length() + std::min(0.0, std::max(d.x, d.y));
   }
};

class UnitedFigure : public Figure {
   const Figure &f1;
   const Figure &f2;
public:
   UnitedFigure (const Figure &_f1, const Figure &_f2) : f1(_f1), f2(_f2) {}
   double distance_to(const Point &p) const override {
       return std::min(f1.distance_to(p), f2.distance_to(p));
   }
};

class ComplementedFigure : public Figure {
   const Figure &f1;
   const Figure &f2;
public:
   ComplementedFigure (const Figure &_f1, const Figure &_f2) : f1(_f1), f2(_f2) {}
   double distance_to(const Point &p) const override {
       return std::max(f1.distance_to(p), -f2.distance_to(p));
   }
};

class IntersectedFigure : public Figure {
   const Figure &f1;
   const Figure &f2;
public:
   IntersectedFigure (const Figure &_f1, const Figure &_f2) : f1(_f1), f2(_f2) {}
   double distance_to(const Point &p) const override {
       return std::max(f1.distance_to(p), f2.distance_to(p));
   }
};

UnitedFigure operator + (const Figure & f1, const Figure & f2) {
   return UnitedFigure{f1, f2};
}

ComplementedFigure operator - (const Figure & f1, const Figure & f2) {
   return ComplementedFigure{f1, f2};
}

IntersectedFigure operator & (const Figure & f1, const Figure & f2) {
   return IntersectedFigure{f1, f2};
}

int main() {
   Point M {};
   std::cin >> M.x >> M.y;
   Circle big(Point{0, 0}, 3);
   Circle small(Point{0, 0}, 2);
   Rectangle quarter_2(Point{0, 0}, Point{-3, 3});
   Rectangle quarter_4(Point{0, 0}, Point{3, -3});
   auto figure = ((big - small) & quarter_2) + (small & quarter_4);
   std::cout << (figure.is_point_into(M) ? "Yes" : "No") << std::endl;
   return 0;
}