#ifndef VECTOR_H
#define VECTOR_H
class Vector {
private:
	long double elements[2];
public:
	Vector(long double a=0, long double b=0) {
		elements[0] = a;
		elements[1] = b;
	}
	long double direction();
	long double magnitude();
	const Vector operator + (const Vector &vector) const {
		return Vector {(*this)[0]+vector[0],(*this)[1]+vector[1]};
	};
	Vector & operator += (const Vector vector) {
		return *this = *this + vector;
	};
	long double & operator [] (size_t n) {return elements[n];}
	const long double & operator [] (size_t n) const {return elements[n];}
	template<class T>
	Vector operator / (T a) const {
		return Vector {(*this)[0]/a,(*this)[1]/a};
	};
};

#endif
