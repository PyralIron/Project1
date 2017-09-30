#ifndef PLANET_H
#define PLANET_H

enum Color {
	BLACK,
	BLUE,
	RED,
	YELLOW,
	NUMCOLORS
};

extern float colors[NUMCOLORS][3];

class Planet {
public:
	std::string name;
	Point pos;
	Vector vel;
	long double mass;
	long double radius;
	Color color;
public:
	//Planet (std::string _name="", Point _pos={0,0}, Vector _velocity={0,0}, long double _radius=0, long double _mass = 0, Color _color=YELLOW), name(_name), pos(_pos), velocity(_velocity), radius(_radius), mass(_mass), color(_color) {};
	static constexpr long double G {6.67408};
	Vector gforce(Planet b);

	const Point &getposition() {return this->pos;}
	const Vector getvelocity() {return this->vel;}
	long double getmass() {return this->mass;}
	std::string getname() {return this->name;}
	Color getcolor() {return this->color;}
	const long double &getradius() {return this->radius;}

	Point &position() {return this->pos;}
	Vector &velocity() {return this->vel;}
};

#endif
