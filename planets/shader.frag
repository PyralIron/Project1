#version 130

uniform vec3 color;
uniform vec2 pos;
uniform float radius;
uniform vec2 dimensions;
uniform mat3 camera;
void main() {
	vec3 p = vec3(pos.xy,0);
	float asp = dimensions.x/dimensions.y;
	gl_FragColor = vec4(color,1.0);
	//vec2 s = vec2((scale)*dimensions.x,(scale)*dimensions.y);
	if (asp < 1) {
		p.y *= asp;
	} else {
		p.x /= asp;
	}
	p = camera*vec3(p.xy,1);
	p.xy = vec2 ((p.x+1)*dimensions.x/2.0,(p.y+1)*dimensions.y/2.0);
	if ( (gl_FragCoord.x-p.x)*(gl_FragCoord.x-p.x) + (gl_FragCoord.y-p.y)*(gl_FragCoord.y-p.y) < (radius*dimensions.x)*(radius*dimensions.x/16)) {
		discard;
	}
	//gl_FragColor = vec4(color,1.0);
}
