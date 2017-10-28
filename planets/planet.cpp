#include <string>
#include <array>
#include <math.h>
#include "vector.h"
#include "point.h"
#include "planet.h"

float colors[NUMCOLORS][3] = {{0,0,0},{0,0,1},{1,0,0},{0,1,0}};

Vector Planet::gforce(Planet b) {
	long double r = Point::distance(this->pos,b.pos);
	long double f =  this->mass*b.mass*G/(r*r);
	long double dx = b.pos[0]-this->pos[0];
	long double dy = b.pos[1]-this->pos[1];
	long double dz = b.pos[2]-this->pos[2];
	if (r!=0) {
		return Vector {f*dx/r, f*dy/r, f*dz/r};
	}
	else {
		return Vector {0,0,0};
	}
}

