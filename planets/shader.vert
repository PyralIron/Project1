attribute vec4 quad;
attribute vec4 col;
uniform vec2 pos;
uniform float radius;
uniform mat4 m2w;
uniform mat4 camera;
varying vec4 outcol;
void main() {
	//vec3 pxyz;
	//pxyz = camera*vec3 ((pos.x+radius*quad.x),(pos.y+radius*quad.y),1);
	gl_Position = camera*m2w*quad;
	//gl_Position = quad;
	outcol = col;
}
