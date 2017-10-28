#include <array>
#include <math.h>
#include "vector.h"
#include "point.h"

long double Point::distance(Point a, Point b) {
	return sqrt((a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1])+(a[2]-b[2])*(a[2]-b[2]));
}
