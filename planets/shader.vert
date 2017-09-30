attribute vec4 quad;
uniform vec2 pos;
uniform float scale;
uniform vec2 dimensions;
void main() {
	float asp = dimensions.x/dimensions.y;
	if (asp < 1.0) {
		gl_Position = vec4 ((pos.x+scale*quad.x),(pos.y+scale*quad.y)*asp,0,1);
	} else {
		gl_Position = vec4 ((pos.x+scale*quad.x)/asp,(pos.y+scale*quad.y),0,1);
	}
	//gl_Position = vec4(pos.x+scale*quad.x,(pos.y+scale*quad.y),0,1);
	//gl_PointSize = scale;
}
