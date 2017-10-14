attribute vec4 quad;
uniform vec2 pos;
uniform float radius;
uniform vec2 dimensions;
uniform mat3 camera;
void main() {
	float asp = dimensions.x/dimensions.y;
	vec3 pxyz;
	if (asp < 1.0) {
		pxyz = camera*vec3 ((pos.x+radius*quad.x),(pos.y+radius*quad.y)*asp,1);
	} else {
		pxyz = camera*vec3 ((pos.x+radius*quad.x)/asp,(pos.y+radius*quad.y),1);
	}
	gl_Position = vec4(pxyz.xy, 0, 1);
}
