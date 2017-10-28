#ifndef CAMERA_H
#define CAMERA_H
#include <cmath>
class Camera
{
public:
	long double width;
	long double height;
	Point position;
	Vector orientation;
	void translate(long double x, long double y, long double z) {
		this->position[0] += x;
	 	this->position[1] += y;
		this->position[2] += z;
	}
	void setpos(long double x, long double y, long double z) {
		this->position[0] = x;
		this->position[1] = y;
		this->position[2] = z;
	}
	void rotate(long double angle) {
		/* hack!!! */ this->orientation[0] = std::fmod(this->orientation[0]+angle,2*3.1415926536);
	}
};

#endif /*CAMERA_H*/
