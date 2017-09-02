#ifndef POINT_H
#define POINT_H

class Point : public Vector
{
public:
	Point (long double a=0, long double b=0) : Vector(a,b) {}
	long double distance(Point b);
	static long double distance(Point a, Point b);
	Point operator + (const Vector &vector) const {
		return Point( (*this)[0]+vector[0], (*this)[1]+vector[1]);
	}
};

#endif  /* POINT_H */
