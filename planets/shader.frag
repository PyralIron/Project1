#version 130

uniform vec3 color;
uniform vec2 pos;
uniform float scale;
uniform vec2 dimensions;
void main() {
	vec2 p = pos;
	float asp = dimensions.x/dimensions.y;
	gl_FragColor = vec4(color,1.0);
	//vec2 s = vec2((scale)*dimensions.x,(scale)*dimensions.y);
	if (asp < 1) {
		p.y *= asp;
	} else {
		p.x /= asp;
	}
	p.xy = vec2 ((p.x+1)*dimensions.x/2.0,(p.y+1)*dimensions.y/2.0);
	if ( (gl_FragCoord.x-p.x)*(gl_FragCoord.x-p.x) + (gl_FragCoord.y-p.y)*(gl_FragCoord.y-p.y) > (scale*dimensions.x)*(scale*dimensions.x/16)) {
		discard;
	}
	//gl_FragColor = vec4(color,1.0);
}
