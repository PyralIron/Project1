#include <array>
#include "vector.h"
#include "point.h"
#include<math.h>

long double Point::distance(Point a, Point b) {
	return sqrt((a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1]));
}
