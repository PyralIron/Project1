#ifndef CAMERA_H
#define CAMERA_H
#include <cmath>
class Camera
{
public:
	long double width;
	long double height;
	Point position;
	Vector roll;
	Vector yaw;
	Vector pitch;
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
	void rpitch(long double angle) {
		auto ori = this->pitch;
                auto s = (angle+ori.magnitude())/ori.magnitude();
                this->pitch = ori*s;
		/* hack!!! */ //this->orientation[0] = std::fmod(this->orientation[0]+angle,2*3.1415926536);
	}
	void ryaw(long double angle) {
		auto ori = this->yaw;
		auto s = (angle+ori.magnitude())/ori.magnitude();
                this->yaw = ori*s;
		//auto theta = ori.magnitude()*2*3.1415926536;
	}
	void rroll(long double angle) {
		auto ori = this->roll;
       		auto s = (angle+ori.magnitude())/ori.magnitude();
        	this->roll = ori*s;

	}
};

#endif /*CAMERA_H*/
