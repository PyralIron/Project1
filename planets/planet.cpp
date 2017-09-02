#include <string>
#include <array>
#include "vector.h"
#include "point.h"
#include "planet.h"

Vector Planet::gforce(Planet b) {
	long double r = Point::distance(this->pos,b.pos);
	long double f =  this->mass*b.mass*G/(r*r);
	long double dx = b.pos[0]-this->pos[0];
	long double dy = b.pos[1]-this->pos[1];
	return Vector {f*dx/r, f*dy/r};
}

