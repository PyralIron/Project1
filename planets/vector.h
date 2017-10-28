
#ifndef VECTOR_H
#define VECTOR_H
class Vector {
protected:
	long double elements[3];
public:
	Vector(long double a=0, long double b=0, long double c=0) {
		elements[0] = a;
		elements[1] = b;
		elements[2] = c;
	}
	long double magnitude() {
        	return sqrt(this->elements[0]*this->elements[0]+this->elements[1]*this->elements[1]+this->elements[2]*this->elements[2]);
	}
	Vector & normalize() {
        	auto mag = Vector::magnitude();
       		this->elements[0] /= mag;
        	this->elements[1] /= mag;
        	this->elements[2] /= mag;
        	return *this;
	}


	const Vector operator + (const Vector &vector) const {
		return Vector {(*this)[0]+vector[0],(*this)[1]+vector[1],(*this)[2]+vector[2]};
	}
	Vector & operator += (const Vector vector) {
		return *this = *this + vector;
	}
	template<class T>
	Vector operator * (T a) const {
		return Vector {(*this)[0]*a,(*this)[1]*a,(*this)[2]*a};
	}
	long double & operator [] (size_t n) {return elements[n];}
	const long double & operator [] (size_t n) const {return elements[n];}
	template<class T>
	Vector operator / (T a) const {
		return Vector {(*this)[0]/a,(*this)[1]/a,(*this)[2]/a};
	}
};

#endif
