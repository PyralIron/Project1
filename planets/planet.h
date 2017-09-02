#ifndef PLANET_H
#define PLANET_H

enum Color {
	BLACK,
	BLUE = 0x000000ff,
	RED = 0x00ff0000,
	YELLOW = 0x0000ffff
};

class Planet {
public:
	std::string name;
	Point pos;
	Vector velocity;
	long double mass;
	long double radius;
	Color color;
public:
	//Planet (std::string _name="", Point _pos={0,0}, Vector _velocity={0,0}, long double _radius=0, long double _mass = 0, Color _color=YELLOW), name(_name), pos(_pos), velocity(_velocity), radius(_radius), mass(_mass), color(_color) {};
	static constexpr long double G {6.67408*0.00000000001};
	Vector gforce(Planet b);

	const Point &getposition() {return this->pos;}
	const Vector getvelocity() {return this->velocity;}
	long double getmass() {return this->mass;}
	std::string getname() {return this->name;}
	Color getcolor() {return this->color;}
	const long double &getradius() {return this->radius;}

	Point &setposition() {return this->pos;}
	Vector &setvelocity() {return this->velocity;}
};

#endif
