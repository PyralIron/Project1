#ifndef CAMERA_H
#define CAMERA_H
#include <cmath>
class Camera
{
public:
	long double width;
	long double height;
	Point position;
	long double orientation;
	void translate(long double x, long double y) {
		this->position[0] += x;
	 	this->position[1] += y;
	}
	void setpos(long double x, long double y) {
		this->position[0] = x;
		this->position[1] = y;
	}
	void rotate(long double angle) {
		this->orientation = std::fmod(this->orientation+angle,2*3.1415926536);
	}
};

#endif /*CAMERA_H*/
